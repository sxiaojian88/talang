from befh.restful_api_socket import RESTfulApiSocket
from befh.exchange import ExchangeGateway
from befh.market_data import L2Depth, Trade
from befh.util import Logger
from befh.instrument import Instrument
from befh.sql_client_template import SqlClientTemplate
#import befh.huobipro.HuobiService as hbs
from functools import partial
from datetime import datetime
import threading
import time


class ExchGwApiHuobiPro(RESTfulApiSocket):
    """
    Exchange gateway RESTfulApi
    """
    def __init__(self):
        RESTfulApiSocket.__init__(self)
    
    @classmethod
    def get_order_book_timestamp_field_name(cls):
        return 'ts'
    
    @classmethod
    def get_trades_timestamp_field_name(cls):
        return 'ts'
        
    @classmethod
    def get_trades_timestamp_format(cls):
        return '%Y-%m-%dT%H:%M:%S.%f'
    
    @classmethod
    def get_bids_field_name(cls):
        return 'bids'
        
    @classmethod
    def get_asks_field_name(cls):
        return 'asks'
        
    @classmethod
    def get_price_field_name(cls):
        return "price"
        
    @classmethod
    def get_volume_field_name(cls):
        return "amount"
        
    @classmethod
    def get_trade_price_field_name(cls):
        return 'price'        
        
    @classmethod
    def get_trade_volume_field_name(cls):
        return 'amount'   
        
    @classmethod
    def get_trade_side_field_name(cls):
        return 'direction'
        
    @classmethod
    def get_trade_id_field_name(cls):
        return 'id'
        
    @classmethod
    def get_order_book_link(cls, instmt):
        #/market/depth?symbol=ethusdt&type=step1
        return "https://api.huobi.pro/market/depth?symbol=%s&type=step5"% instmt.get_instmt_code()

    @classmethod
    def get_trades_link(cls, instmt):
        return "https://api.huobi.pro/market/trade?symbol=%s"% instmt.get_instmt_code()
                
    @classmethod
    def parse_l2_depth(cls, instmt, raw):
        """
        Parse raw data to L2 depth
        :param instmt: Instrument
        :param raw: Raw data in JSON
        """
        """
         {'bids': [[13700.8, 1.2389], [13700.5, 2.1162], [13700.2, 0.0352], [13700.0, 0.1149], [13686.1, 0.1], [13686.0, 0.005], [13680.0, 0.1524], [13675.3, 0.1], [13665.2, 0.8], [13664.7, 0.132], [13664.6, 0.0329], [13651.4, 0.297], [13651.3, 0.0383], [13650.0, 0.0011], [13645.2, 1.3241], [13639.5, 0.1198], [13622.0, 0.003], [13616.0, 0.01], [13603.0, 1.6498], [13600.0, 0.4871]], 'asks': [[13730.0, 0.005], [13732.3, 0.0228], [13736.9, 0.8], [13740.0, 2.6722], [13740.4, 0.2431], [13740.6, 0.4722], [13740.9, 0.0998], [13743.2, 0.063], [13745.0, 0.0276], [13756.9, 1.3241], [13766.0, 1.6502], [13767.9, 0.188], [13768.0, 0.2877], [13787.6, 0.439], [13790.0, 0.7925], [13798.0, 0.0187], [13800.0, 6.2271], [13800.2, 0.1055], [13829.0, 0.03189167691083954], [13833.0, 0.2172]], 'ts': 1515743657029, 'version': 1184504329}
        """
        
        l2_depth = L2Depth()
    
        #raw = raw["result"]
        
        keys = list(raw.keys())
        
        #Logger.info(cls.__name__, "keys:%s" %keys)

        if cls.get_bids_field_name() in keys and \
           cls.get_asks_field_name() in keys:
            
            # Date time
            timestamp = float(raw[cls.get_order_book_timestamp_field_name()])/1000.0
            l2_depth.date_time = datetime.utcfromtimestamp(timestamp).strftime("%Y%m%d %H:%M:%S.%f")
            #Logger.info(cls.__name__,"date_time:%s.........."%l2_depth.date_time)
            # Bids
            bids = raw[cls.get_bids_field_name()]
            bids = sorted(bids, key=lambda x: x[0], reverse=True)
            #Logger.info(cls.__name__,"len(bids):%d"%len(bids))
            #Logger.info(cls.__name__,"bids:%s"%bids)

            for i in range(0, 5):#len(bids)):
                #Logger.info(cls.__name__,"bids:%d.........."%i)
                l2_depth.bids[i].price = float(bids[i][0]) if type(bids[i][0]) != float else bids[i][0]
                l2_depth.bids[i].volume = float(bids[i][1]) if type(bids[i][1]) != float else bids[i][1]   
                
            # Asks
            asks = raw[cls.get_asks_field_name()]
            asks = sorted(asks, key=lambda x: x[0])
            #Logger.info(cls.__name__,"asks:%s"%asks)
            for i in range(0, 5):#len(asks)):
                #Logger.info(cls.__name__,"asks:%d.........."%i)
                l2_depth.asks[i].price = float(asks[i][0]) if type(asks[i][0]) != float else asks[i][0]
                l2_depth.asks[i].volume = float(asks[i][1]) if type(asks[i][1]) != float else asks[i][1]        
            #Logger.info(cls.__name__,"if cls.get_bids_field_name() in keys")
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
        
        """
        {'id': 17592355736499, 'amount': 0.0972, 'price': 13802.66, 'direction': 'buy', 'ts': 1515800691239}
        """
        
        trade = Trade()
        keys = list(raw.keys())
        
        if cls.get_trades_timestamp_field_name() in keys and \
           cls.get_trade_id_field_name() in keys and \
           cls.get_trade_side_field_name() in keys and \
           cls.get_trade_price_field_name() in keys and \
           cls.get_trade_volume_field_name() in keys:
        
            # Date time
            #date_time = raw[cls.get_trades_timestamp_field_name()]
            timestamp = float(raw[cls.get_order_book_timestamp_field_name()])/1000.0
            trade.date_time  = datetime.utcfromtimestamp(timestamp).strftime("%Y%m%d %H:%M:%S.%f")
                 
            # Trade side
            trade.trade_side = 1 if raw[cls.get_trade_side_field_name()] == 'buy' else 2
                
            # Trade id
            trade.trade_id = str(raw[cls.get_trade_id_field_name()])
            
            # Trade price
            trade.trade_price = float(str(raw[cls.get_trade_price_field_name()]))
            
            # Trade volume
            trade.trade_volume = float(str(raw[cls.get_trade_volume_field_name()]))
        else:
            raise Exception('Does not contain trade keys in instmt %s-%s.\nOriginal:\n%s' % \
                (instmt.get_exchange_name(), instmt.get_instmt_name(), \
                 raw))        

        return trade

    @classmethod
    def get_order_book(cls, instmt):
        """
        Get order book
        :param instmt: Instrument
        :return: Object L2Depth
        """
        """
        Original:
        {'status': 'ok', 'ch': 'market.btcusdt.depth.step5', 'ts': 1515743658032, 'tick': {'bids': [[13700.8, 1.2389], [13700.5, 2.1162], [13700.2, 0.0352], [13700.0, 0.1149], [13686.1, 0.1], [13686.0, 0.005], [13680.0, 0.1524], [13675.3, 0.1], [13665.2, 0.8], [13664.7, 0.132], [13664.6, 0.0329], [13651.4, 0.297], [13651.3, 0.0383], [13650.0, 0.0011], [13645.2, 1.3241], [13639.5, 0.1198], [13622.0, 0.003], [13616.0, 0.01], [13603.0, 1.6498], [13600.0, 0.4871]], 'asks': [[13730.0, 0.005], [13732.3, 0.0228], [13736.9, 0.8], [13740.0, 2.6722], [13740.4, 0.2431], [13740.6, 0.4722], [13740.9, 0.0998], [13743.2, 0.063], [13745.0, 0.0276], [13756.9, 1.3241], [13766.0, 1.6502], [13767.9, 0.188], [13768.0, 0.2877], [13787.6, 0.439], [13790.0, 0.7925], [13798.0, 0.0187], [13800.0, 6.2271], [13800.2, 0.1055], [13829.0, 0.03189167691083954], [13833.0, 0.2172]], 'ts': 1515743657029, 'version': 1184504329}}

        """
        res = cls.request(cls.get_order_book_link(instmt))
        
        #res= hbs.get_depth(instmt.get_instmt_code(), "step5","true")
        res=res["tick"]

        #Logger.info(cls.__name__, "get_order_book:%s" %res)
        #Logger.info(cls.__name__, "get_order_book...")
        if len(res) > 0:
            return cls.parse_l2_depth(instmt=instmt,
                                       raw=res)
        else:
            return None

    @classmethod
    def get_trades(cls, instmt):
        """
        Get trades
        :param instmt: Instrument
        :param trade_id: Trade id
        :return: List of trades
        """
        """
        {'status': 'ok', 'ch': 'market.btcusdt.trade.detail', 'ts': 1515800693890, 'tick': {'id': 1202210735, 'ts': 1515800691239, 'data': [{'id': 17592355736499, 'amount': 0.0972, 'price': 13802.66, 'direction': 'buy', 'ts': 1515800691239}, {'id': 17592355736498, 'amount': 0.075, 'price': 13802.61, 'direction': 'buy', 'ts': 1515800691239}]}}
        """
        link = cls.get_trades_link(instmt)
        res = cls.request(link)
        #res=hbs.get_trade(instmt.get_instmt_code())
        
        #Logger.info(cls.__name__, "get_trades:%s" %res)
        
        res = res["tick"]
        res = res["data"]
        trades = []
        if len(res) > 0:
            for i in range(len(res)-1, -1, -1):
                trade = cls.parse_trade(instmt=instmt,
                                         raw=res[i])
                trades.append(trade)

        return trades


class ExchGwHuobiPro(ExchangeGateway):
    """
    Exchange gateway HuobiPro
    """
    def __init__(self, db_clients):
        """
        Constructor
        :param db_client: Database client
        """
        ExchangeGateway.__init__(self, ExchGwApiHuobiPro(), db_clients)

    @classmethod
    def get_exchange_name(cls):
        """
        Get exchanges name
        :return: Exchange name string
        """
        return 'HuobiPro'

    def get_order_book_worker(self, instmt):
        """
        Get order book worker
        :param instmt: Instrument
        """
        while True:
            try:
                l2_depth = self.api_socket.get_order_book(instmt)
                #Logger.info(self.__class__.__name__,"get_order_book_worker....1")
                if l2_depth is not None and l2_depth.is_diff(instmt.get_l2_depth()):
                    #Logger.info(self.__class__.__name__,"get_order_book_worker...")
                    instmt.set_prev_l2_depth(instmt.get_l2_depth())
                    instmt.set_l2_depth(l2_depth)
                    instmt.incr_order_book_id()
                    self.insert_order_book(instmt)
            except Exception as e:
                Logger.error(self.__class__.__name__, "Error in order book: %s" %e)
            time.sleep(1)

    def get_trades_worker(self, instmt):
        """
        Get order book worker thread
        :param instmt: Instrument name
        """
        while True:
            try:
                ret = self.api_socket.get_trades(instmt)
                if ret is None or len(ret) == 0:
                    time.sleep(1)
                    continue
            except Exception as e:
                Logger.error(self.__class__.__name__, "Error in trades: %s" % e)                
                
            for trade in ret:
                assert isinstance(trade.trade_id, str), "trade.trade_id(%s) = %s" % (type(trade.trade_id), trade.trade_id)
                assert isinstance(instmt.get_exch_trade_id(), str), \
                       "instmt.get_exch_trade_id()(%s) = %s" % (type(instmt.get_exch_trade_id()), instmt.get_exch_trade_id())
                if int(trade.trade_id) > int(instmt.get_exch_trade_id()):
                    instmt.set_exch_trade_id(trade.trade_id)
                    instmt.incr_trade_id()
                    self.insert_trade(instmt, trade)
            
            # After the first time of getting the trade, indicate the instrument
            # is recovered
            if not instmt.get_recovered():
                instmt.set_recovered(True)

            time.sleep(1)

    def start(self, instmt):
        """
        Start the exchanges gateway
        :param instmt: Instrument
        :return List of threads
        """
        instmt.set_l2_depth(L2Depth(5))
        instmt.set_prev_l2_depth(L2Depth(5))
        instmt.set_instmt_snapshot_table_name(self.get_instmt_snapshot_table_name(instmt.get_exchange_name(),
                                                                                  instmt.get_instmt_name()))
        self.init_instmt_snapshot_table(instmt)
        instmt.set_recovered(False)
        t1 = threading.Thread(target=partial(self.get_order_book_worker, instmt))
        t2 = threading.Thread(target=partial(self.get_trades_worker, instmt))
        t1.start()
        t2.start()
        return [t1, t2]
        
        
if __name__ == '__main__':
    Logger.init_log()
    exchange_name = 'HuobiPro'
    instmt_name = 'BTCETH'
    instmt_code = 'BTCETH'
    instmt = Instrument(exchange_name, instmt_name, instmt_code)    
    db_client = SqlClientTemplate()
    exch = ExchGwHuobiPro([db_client])
    instmt.set_l2_depth(L2Depth(5))
    instmt.set_prev_l2_depth(L2Depth(5))
    instmt.set_recovered(False)    
    # exch.get_order_book_worker(instmt)
    exch.get_trades_worker(instmt)