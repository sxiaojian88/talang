# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util
import talang.util.util_data as ut

# 现货API
okexcoinSpot = okex_util.getOkcoinSpot()

# 期货API
okexcoinFuture = okex_util.getOkcoinFuture()


class ExchangeQuoteApi():

        def get_buy_1_value(self, exchange, base_coin, quote_coin):
            ex_qt = ExchangeQuoteApi()
            msg = ex_qt.get_msg(exchange, base_coin, quote_coin)
            buy_1_price = float(msg['buy'])

            return buy_1_price

        def get_sell_1_value(self, exchange, base_coin, quote_coin):
            ex_qt = ExchangeQuoteApi()
            msg = ex_qt.get_msg(exchange, base_coin, quote_coin)
            sell_1_price = float(msg['sell'])

            return sell_1_price

        @classmethod
        def get_msg(cls, exchange, base_coin, quote_coin):
            # 组合symbol值
            symbol = ut.get_symbol(exchange, base_coin, quote_coin)
            msg = ''
            if ut.okex_exchange.lower() == exchange.lower():
                msg = okexcoinSpot.ticker(str.lower(symbol))
                #print(msg)
                msg = msg["ticker"]
                #print(msg)
            else:
                print('no support exchange')

            return msg


if __name__ == '__main__':
    ex_qt = ExchangeQuoteApi()
    exchange_name = 'okex'
    base_coin = 'btc'
    quote_coin = 'usdt'
    #ex_qt.get_msg(exchange_name, base_coin, quote_coin)
    buy_1 = ex_qt.get_buy_1_value(exchange_name, base_coin, quote_coin)
    print("exchange_quote get buy_1:%f" % buy_1)
    buy_1 = ex_qt.get_sell_1_value(exchange_name, base_coin, quote_coin)
    print("exchange_quote get sell_1:%f" % buy_1)