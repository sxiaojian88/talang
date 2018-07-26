#!/usr/bin/env python

import talang.trader.trade.spot_trade_batch as spot_batch_trad_api
from talang.util.model.Trade import Trade
import collections

trade_one = collections.namedtuple('trade_one', 'price amount type')


def main():

    #T302-okex-批量-定价-卖出-交易(特定币种)，每次只能发送5笔
    #============输入参数==============================
    base_coin = 'xrp'
    quote_coin = 'usdt'
    prices = [5, 6, 7, 8, 9]
    amounts = [1, 2, 3, 4, 5]
    # ================================================

    ex_qt = spot_batch_trad_api.SpotBatchTrade()
    exchange_name = 'okex'
    tradeType = 'sell'
    types =['sell', 'sell', 'sell', 'sell', 'sell', 'sell', 'sell', 'sell']

    #orders_data = ex_qt.get_orders_data(exchange_name, base_coin, quote_coin, prices, amounts, types)
    #print(orders_data)
    #tk = ex_qt.get_spot_batch_trade_result(exchange_name, base_coin, quote_coin, tradeType, orders_data)


    tk = ex_qt.spot_batch_trade(exchange_name, base_coin, quote_coin, tradeType, prices, amounts, types)
    print('result:%s' % tk.result + ',trade_id:%s' % tk.trade_id)

if __name__ == "__main__":
    main()
