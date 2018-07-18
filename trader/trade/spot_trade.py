# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util
import talang.util.util_data as ut
from datetime import datetime
from talang.util.model.Trade import Trade
# 现货API
okexcoinSpot = okex_util.getOkcoinSpot()
# 期货API
okexcoinFuture = okex_util.getOkcoinFuture()


class SpotTrade:

        def get_spot_trade_result(self, exchange, base_coin, quote_coin, tradeType, price='', amount=''):
            '''
            # Response
            {"result":true,"order_id":123456}
            '''
            trade = Trade()
            ex_qt = SpotTrade()
            msg = ex_qt.post_trade(exchange, base_coin, quote_coin, tradeType, price, amount)
            trade.Result = msg['result']    #'result': True
            trade.Trade_id = msg['order_id']
            trade.price = price
            trade.amount = amount
            trade.exchange = exchange
            trade.time = datetime.now().strftime("%Y%m%d %H:%M:%S.%f")

            return trade


        @classmethod
        def post_trade(cls, exchange, base_coin, quote_coin, tradeType, price='', amount=''):
            # 组合symbol值
            symbol = ut.get_symbol(exchange, base_coin, quote_coin)
            msg = ''
            #    def trade(self, symbol, tradeType, price='', amount=''):
            if ut.okex_exchange.lower() == exchange.lower():
                msg = okexcoinSpot.trade(symbol, tradeType, price, amount)
                print(msg)
                # {"result":true,"order_id":123456}
            else:
                print('no support exchange')

            return msg

if __name__ == '__main__':
    ex_qt = SpotTrade()
    exchange_name = 'okex'
    base_coin = 'eos'
    quote_coin = 'usdt'
    tradeType = 'sell'
    price = 108
    amount = 1
    tk = Trade()
    tk = ex_qt.get_spot_trade_result(exchange_name, base_coin, quote_coin, tradeType, price, amount)
    print('result:%s' %tk.Result + 'trade_id:%s' %tk.Trade_id)
