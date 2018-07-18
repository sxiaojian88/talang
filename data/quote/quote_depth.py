# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util
import talang.util.util_data as ut

# 现货API
okexcoinSpot = okex_util.getOkcoinSpot()

# 期货API
okexcoinFuture = okex_util.getOkcoinFuture()


class QuoteDepth():

        def get_buy_1_value(self, exchange, base_coin, quote_coin, size=1):
            ex_qt = QuoteDepth()
            msg = ex_qt.get_msg(exchange, base_coin, quote_coin, size)
            bids = msg['bids']
            bids = sorted(bids, key=lambda x: x[0], reverse=True)
            print(bids)
            buy_1_price = bids[0][0]

            return buy_1_price

        def get_sell_1_value(self, exchange, base_coin, quote_coin, size=1):
            ex_qt = QuoteDepth()
            msg = ex_qt.get_msg(exchange, base_coin, quote_coin, size)
            asks = msg['asks']
            asks = sorted(asks, key=lambda x: x[0])
            print(asks)
            sell_1_price = asks[0][0]

            return sell_1_price

        @classmethod
        def get_msg(cls, exchange, base_coin, quote_coin, size=1):
            # 组合symbol值
            symbol = ut.get_symbol(exchange, base_coin, quote_coin)
            msg = ''
            if ut.okex_exchange.lower() == exchange.lower():
                msg = okexcoinSpot.depth(str.lower(symbol), size)
                print(msg)
            else:
                print('no support exchange')

            return msg


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