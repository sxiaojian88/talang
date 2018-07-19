# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util
import talang.data.quote.quote_depth as qt_depth
import talang.util.util_data as ut
from datetime import datetime
from talang.util.model.Trade import Trade

# 现货API
okexcoinSpot = okex_util.getOkcoinSpot()
# 期货API
okexcoinFuture = okex_util.getOkcoinFuture()


class SpotTradeRule:

        def if_right_price(self, exchange, base_coin, quote_coin, tradeType, price):
            '''
            tradeType='buy' price需比depth中sell1要小，大则返回False
            tradeType='sell' price需对比depth中buy1要大，小则返回False
            '''
            qt_d = qt_depth.QuoteDepth()
            if str.lower(tradeType) == 'buy' or str.lower(tradeType) == 'buy_market':
                sell1 = qt_d.get_sell_1_value(exchange, base_coin, quote_coin, 5)
                if price < sell1:
                    return True
            elif str.lower(tradeType) == 'sell' or str.lower(tradeType) == 'sell_market':
                buy1 = qt_d.get_buy_1_value(exchange, base_coin, quote_coin, 5)
                if price > buy1:
                    return True

            return False

        def if_right_amount(self, exchange, base_coin, quote_coin, tradeType, amount):

            return True

if __name__ == '__main__':
    ex_qt = SpotTradeRule()
    exchange_name = 'okex'
    base_coin = 'eos'
    quote_coin = 'usdt'
    tradeType = 'sell'
    price = 8.8

    print(ex_qt.if_right_price(exchange_name,base_coin,quote_coin,tradeType,price))

