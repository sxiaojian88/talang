#!/usr/bin/env python

import talang.trader.trade.spot_batch_trade as spot_batch_trad_api;
from talang.util.model.Trade import Trade

def main():

    ex_qt = spot_batch_trad_api.SpotBatchTrade()
    exchange_name = 'okex'
    base_coin = 'eos'
    quote_coin = 'usdt'
    tradeType = 'sell'
    '''
    [{price:3,amount:5,type:'sell'},{price:3,amount:3,type:'buy'}]
    '''
    orders_data = ''
    tk = ex_qt.get_spot_batch_trade_result(exchange_name, base_coin, quote_coin, tradeType, orders_data)
    print('result:%s' % tk.Result + ',trade_id:%s' % tk.Trade_id)

if __name__ == "__main__":
    main()
