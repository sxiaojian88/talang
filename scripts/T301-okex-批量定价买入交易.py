#!/usr/bin/env python

import talang.trader.trade.spot_trade_batch as spot_batch_trad_api
from talang.util.model.Trade import Trade
import collections

trade_one = collections.namedtuple('trade_one', 'price amount type')


def main():

    ex_qt = spot_batch_trad_api.SpotBatchTrade()
    exchange_name = 'okex'
    base_coin = 'eos'
    quote_coin = 'usdt'
    tradeType = 'buy'

    '''
    [{price:3,amount:5,type:'sell'},{price:3,amount:3,type:'buy'}]
    '''
    prices = [3, 3.5, 4, 88, 99, 110, 220]
    amounts = [1, 2, 3, 4, 5, 6, 7, 8]
    types =['buy', 'buy', 'buy', 'buy', 'buy', 'buy', 'buy', 'buy']

    orders_data = ex_qt.get_orders_data(exchange_name, base_coin, quote_coin, prices, amounts, types)
    print(orders_data)
    #tk = ex_qt.get_spot_batch_trade_result(exchange_name, base_coin, quote_coin, tradeType, orders_data)


    #tk = ex_qt.get_spot_batch_trade(exchange_name, base_coin, quote_coin, tradeType, prices, amounts, types)
    #print('result:%s' % tk.Result + ',trade_id:%s' % tk.Trade_id)

if __name__ == "__main__":
    main()
