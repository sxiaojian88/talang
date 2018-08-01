# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util
import talang.util.util_data as ut
import time
from talang.util.Logger import Logger
# 现货API
okexcoinSpot = okex_util.getOkcoinSpot()

# 期货API
okexcoinFuture = okex_util.getOkcoinFuture()


class QuoteDepth():


    def get_buy1_and_sell1(self, exchange, base_coin, quote_coin, size=5):
        ex_qt = QuoteDepth()
        msg = ex_qt.get_msg(exchange, base_coin, quote_coin, size)
        #print(msg)
        bids = msg['bids']
        bids = sorted(bids, key=lambda x: x[0], reverse=True)
        #print(bids)
        buy_1_price = bids[0][0]
        buy_1_volume = bids[0][1]

        asks = msg['asks']
        asks = sorted(asks, key=lambda x: x[0])
        #print(asks)
        sell_1_price = asks[0][0]
        sell_1_volume = asks[0][1]

        return buy_1_price, sell_1_price, buy_1_volume, sell_1_volume


    def get_buy_1_value(self, exchange, base_coin, quote_coin, size=5):
        ex_qt = QuoteDepth()
        msg = ex_qt.get_msg(exchange, base_coin, quote_coin, size)
        bids = msg['bids']
        bids = sorted(bids, key=lambda x: x[0], reverse=True)
        #print(bids)
        buy_1_price = bids[0][0]

        return buy_1_price

    def get_sell_1_value(self, exchange, base_coin, quote_coin, size=5):
        ex_qt = QuoteDepth()
        msg = ex_qt.get_msg(exchange, base_coin, quote_coin, size)
        asks = msg['asks']
        asks = sorted(asks, key=lambda x: x[0])
        #print(asks)
        sell_1_price = asks[0][0]

        return sell_1_price

    @classmethod
    def get_bids(cls, exchange, base_coin, quote_coin, size=5):
        ex_qt = QuoteDepth()
        msg = ex_qt.get_msg(exchange, base_coin, quote_coin, size)
        bids = msg[cls.get_bids_field_name()]
        bids = sorted(bids, key=lambda x: x[0], reverse=True)
        return bids

    @classmethod
    def get_asks(cls, exchange, base_coin, quote_coin, size=5):
        ex_qt = QuoteDepth()
        msg = ex_qt.get_msg(exchange, base_coin, quote_coin, size)
        asks = msg[cls.get_asks_field_name()]
        asks = sorted(asks, key=lambda x: x[0])
        return asks

    @classmethod
    def get_msg(cls, exchange, base_coin, quote_coin, size=5):
        # 组合symbol值
        symbol = ut.get_symbol(exchange, base_coin, quote_coin)
        msg = ''
        if ut.okex_exchange.lower() == exchange.lower():
            i = 1
            while True:
                try:
                    msg = okexcoinSpot.depth(str.lower(symbol), size)
                    keys = list(msg.keys())
                    if cls.get_bids_field_name() in keys and \
                            cls.get_asks_field_name() in keys:
                        return msg
                    else:
                        i = i + 1
                        time.sleep(1)
                except Exception as e:
                    Logger.error(cls.__class__.__name__, "Error in get_msg: %s" % e)
                    i = i + 1
                    time.sleep(1)
                if i > ut.RE_TRY_TIMES:
                    return None
        else:
            Logger.error(cls.__class__.__name__, 'no support exchange')

        return msg

    @classmethod
    def get_bids_field_name(cls):
        return 'bids'

    @classmethod
    def get_asks_field_name(cls):
        return 'asks'

if __name__ == '__main__':
    ex_qt = QuoteDepth()
    exchange_name = 'okex'
    base_coin = 'btc'
    quote_coin = 'usdt'
    size = 5
    #ex_qt.get_msg(exchange_name, base_coin, quote_coin)
    buy_1 = ex_qt.get_buy_1_value(exchange_name, base_coin, quote_coin, size)
    print("exchange_quote get buy_1:%f" % buy_1)
    sell_1 = ex_qt.get_sell_1_value(exchange_name, base_coin, quote_coin, size)
    print("exchange_quote get sell_1:%f" % sell_1)