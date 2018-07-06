# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util
import talang.util.util_data as ut
from datetime import datetime
from talang.util.model.Trade import Trade
# 现货API
okexcoinSpot = okex_util.getOkcoinSpot()
# 期货API
okexcoinFuture = okex_util.getOkcoinFuture()


class spot_batch_trade():

        def get_spot_batch_trade_result(self, exchange, base_coin, quote_coin, tradeType,orders_data):
            '''
            # Response
            {"result":true,"order_id":123456}
            '''
            trade = Trade()
            ex_qt = spot_batch_trade()
            msg = ex_qt.post_trade(exchange, base_coin, quote_coin,tradeType,orders_data)
            trade.Result = msg['result']    #'result': True
            trade.Trade_id = msg['order_id']
            trade.Time = datetime.datetime.now()

            return trade


        @classmethod
        def post_trade(cls, exchange, base_coin, quote_coin,tradeType,orders_data):
            # 组合symbol值
            symbol = ut.get_symbol(exchange, base_coin, quote_coin)
            msg = ''
            #    def batchTrade(self, symbol, tradeType, orders_data):
            if ut.okex_exchange.lower() == exchange.lower():
                msg = okexcoinSpot.batchTrade(symbol, tradeType,orders_data)
                print(msg)
                # {"result":true,"order_id":123456}
            else:
                print('no support exchange')

            return msg

if __name__ == '__main__':
    ex_qt = spot_batch_trade()
    exchange_name = 'okex'
    base_coin = 'eos'
    quote_coin = 'usdt'
    tradeType = 'sell'
    orders_data=''
    tk = ex_qt.get_spot_batch_trade_result(exchange_name, base_coin, quote_coin, tradeType, orders_data)
    print('result:%s' %tk.Result + 'trade_id:%s' %tk.Trade_id)
