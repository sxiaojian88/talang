from befh.ws_api_socket import WebSocketApiClient
from befh.market_data import L2Depth, Trade
from befh.exchanges.gateway import ExchangeGateway
from befh.instrument import Instrument
from befh.util import Logger
import time
import threading
import json
from functools import partial
from datetime import datetime


class ExchGwZbWs(WebSocketApiClient):
    """
    Exchange socket
    """
    def __init__(self):
        """
        Constructor
        """
        WebSocketApiClient.__init__(self, 'ExchGwZb')
        
    @classmethod
    def get_order_book_timestamp_field_name(cls):
        return 'timestamp'
    
    @classmethod
    def get_bids_field_name(cls):
        return 'bids'
        
    @classmethod
    def get_asks_field_name(cls):
        return 'asks'
        
    @classmethod
    def get_link(cls):
        return 'wss://api.zb.com:9999/websocket'
    
    @classmethod
    def get_order_book_subscription_string(cls, instmt):
        return json.dumps({"event":"addChannel", "channel": instmt.get_order_book_channel_id()})

    @classmethod
    def get_trades_subscription_string(cls, instmt):
        return json.dumps({"event":"addChannel", "channel": instmt.get_trades_channel_id()})

    @classmethod
    def parse_l2_depth(cls, instmt, raw):
        """
        Parse raw data to L2 depth
        :param instmt: Instrument
        :param raw: Raw data in JSON
        """
        l2_depth = instmt.get_l2_depth()
        keys = list(raw.keys())
        if cls.get_order_book_timestamp_field_name() in keys and \
           cls.get_bids_field_name() in keys and \
           cls.get_asks_field_name() in keys:
            
            # Date time
            timestamp = float(raw[cls.get_order_book_timestamp_field_name()])/1000.0
            l2_depth.date_time = datetime.utcfromtimestamp(timestamp).strftime("%Y%m%d %H:%M:%S.%f")
            
            # Bids
            bids = raw[cls.get_bids_field_name()]
            bids = sorted(bids, key=lambda x: x[0], reverse=True)
            for i in range(0, len(bids)):
                l2_depth.bids[i].price = float(bids[i][0]) if type(bids[i][0]) != float else bids[i][0]
                l2_depth.bids[i].volume = float(bids[i][1]) if type(bids[i][1]) != float else bids[i][1]   
                
            # Asks
            asks = raw[cls.get_asks_field_name()]
            asks = sorted(asks, key=lambda x: x[0])
            for i in range(0, len(asks)):
                l2_depth.asks[i].price = float(asks[i][0]) if type(asks[i][0]) != float else asks[i][0]
                l2_depth.asks[i].volume = float(asks[i][1]) if type(asks[i][1]) != float else asks[i][1]            
        else:
            raise Exception('Does not contain order book keys in instmt %s-%s.\nOriginal:\n%s' % \
                (instmt.get_exchange_name(), instmt.get_instmt_name(), \
                 raw))        

        return l2_depth

    @classmethod
    def parse_trade(cls, instmt, raw):
        """
        :param instmt: Instrument
        :param raw: Raw data in JSON
        :return:
        """
        trade = Trade()
        trade_id = raw[0]
        trade_price = float(raw[1])
        trade_volume = float(raw[2])
        timestamp = raw[3]
        trade_side = raw[4]
        
        trade.trade_id = trade_id + timestamp
        trade.trade_price = trade_price
        trade.trade_volume = trade_volume
        trade.trade_side = Trade.parse_side(trade_side)

        return trade


class ExchGwZb(ExchangeGateway):
    """
    Exchange gateway
    """
    def __init__(self, db_clients):
        """
        Constructor
        :param db_client: Database client
        """
        ExchangeGateway.__init__(self, ExchGwZbWs(), db_clients)

    @classmethod
    def get_exchange_name(cls):
        """
        Get exchanges name
        :return: Exchange name string
        """
        return 'Zb'

    def on_open_handler(self, instmt, ws):
        """
        Socket on open handler
        :param instmt: Instrument
        :param ws: Web socket
        """
        Logger.info(self.__class__.__name__, "Instrument %s is subscribed in channel %s" % \
                  (instmt.get_instmt_code(), instmt.get_exchange_name()))
        #if not instmt.get_subscribed():
            ##instmt_code_split = instmt.get_instmt_code().split('_')
            ##xie.2018.1.4 begin
        instmt.set_order_book_channel_id("%s_depth" % instmt.get_instmt_code())
        instmt.set_trades_channel_id("%s_trades" % instmt.get_instmt_code())
            ##xie.2018.1.4 end
            
        ws.send(self.api_socket.get_order_book_subscription_string(instmt))
        ws.send(self.api_socket.get_trades_subscription_string(instmt))
        instmt.set_subscribed(True)

    def on_close_handler(self, instmt, ws):
        """
        Socket on close handler
        :param instmt: Instrument
        :param ws: Web socket
        """
        Logger.info(self.__class__.__name__, "Instrument %s is unsubscribed in channel %s" % \
                  (instmt.get_instmt_code(), instmt.get_exchange_name()))
        instmt.set_subscribed(False)

    def on_message_handler(self, instmt, messages):
        """
        Incoming message handler
        :param instmt: Instrument
        :param message: Message
        """
        for message in messages:
            keys = message.keys()
            if 'channel' in keys:
                if message['channel'] == instmt.get_order_book_channel_id():
                    instmt.set_prev_l2_depth(instmt.get_l2_depth().copy())
                    self.api_socket.parse_l2_depth(instmt, message)

                    # Insert only if the first 5 levels are different
                    if instmt.get_l2_depth().is_diff(instmt.get_prev_l2_depth()):
                        instmt.incr_order_book_id()
                        self.insert_order_book(instmt)

                elif message['channel'] == instmt.get_trades_channel_id():
                    for trade_raw in message['data']:
                        trade = self.api_socket.parse_trade(instmt, trade_raw)
                        if trade.trade_id != instmt.get_exch_trade_id():
                            instmt.incr_trade_id()
                            instmt.set_exch_trade_id(trade.trade_id)
                            self.insert_trade(instmt, trade)

            else:
                Logger.info(self.__class__.__name__, ' - ' + json.dumps(message))

    def start(self, instmt):
        """
        Start the exchanges gateway
        :param instmt: Instrument
        :return List of threads
        """
        instmt.set_prev_l2_depth(L2Depth(20))
        instmt.set_l2_depth(L2Depth(20))
        instmt.set_instmt_snapshot_table_name(self.get_instmt_snapshot_table_name(instmt.get_exchange_name(),
                                                                                  instmt.get_instmt_name()))
        self.init_instmt_snapshot_table(instmt)
        return [self.api_socket.connect(self.api_socket.get_link(),
                                        on_message_handler=partial(self.on_message_handler, instmt),
                                        on_open_handler=partial(self.on_open_handler, instmt),
                                        on_close_handler=partial(self.on_close_handler, instmt))]

