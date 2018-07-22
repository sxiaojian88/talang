# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util
import talang.util.util_data as ut
from datetime import datetime
from talang.util.model.Trade import Trade

# 现货API
okexcoinSpot = okex_util.getOkcoinSpot()
# 期货API
okexcoinFuture = okex_util.getOkcoinFuture()


class SpotTradeCancel:

        def get_spot_trade_cancel_result(self, exchange, symbol, order_id):
            '''
            返回值说明
            result:true撤单请求成功，等待系统执行撤单；false撤单失败(用于单笔订单)
            order_id:订单ID(用于单笔订单)
            success:撤单请求成功的订单ID，等待系统执行撤单(用于多笔订单)
            error:撤单请求失败的订单ID(用户多笔订单)
            # Response
            {"result":true,"order_id":123456}
            '''
            trade = Trade()
            ex_qt = SpotTradeCancel()
            msg = ex_qt.post_trade_cancel(exchange, symbol, order_id)
            #print(msg)
            trade.Result = msg['result']    #'result': True
            trade.Trade_id = msg['order_id']

            trade.exchange = exchange
            trade.time = datetime.now().strftime("%Y%m%d %H:%M:%S.%f")

            return trade


        @classmethod
        def post_trade_cancel(cls, exchange, symbol, order_id):
            if ut.okex_exchange.lower() == exchange.lower():
                msg = okexcoinSpot.cancelOrder(symbol, order_id)
                #print(msg)
            else:
                print('no support exchange')
            return msg

if __name__ == '__main__':
    ex_qt = SpotTradeCancel()
    exchange_name = 'okex'
    base_coin = 'eos'
    quote_coin = 'usdt'
    order_id = '637839144'
    tk = Trade()
    tk = ex_qt.get_spot_trade_cancel_result(exchange_name, base_coin, quote_coin, order_id)
    print('result:%s' %tk.Result + 'trade_id:%s' %tk.Trade_id)
