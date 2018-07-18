# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util
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
            tradeType='sell' price需大于buy1价格，对比depth中buy1
            tradeType='buy' price需小于sell1价格，对比depth中sell1

            :param exchange:
            :param base_coin:
            :param quote_coin:
            :param tradeType:
            :param price:
            :return:
            '''

            return True

        def if_right_amount(self, exchange, base_coin, quote_coin, tradeType, amount):

            return True

if __name__ == '__main__':
    ex_qt = SpotTradeRule()
    exchange_name = 'okex'
    base_coin = 'eos'
    quote_coin = 'usdt'
    tradeType = 'sell'
    price = 108

    tk = Trade()

    print('result:%s' %tk.Result + 'trade_id:%s' %tk.Trade_id)
