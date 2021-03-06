# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util
import talang.util.util_data as ut
from datetime import datetime
from talang.util.model.Trade import Trade
import talang.trader.trade.spot_trade_rule as spot_trade_rule
# 现货API
okexcoinSpot = okex_util.getOkcoinSpot()
# 期货API
okexcoinFuture = okex_util.getOkcoinFuture()

class SpotBatchTrade:

        def spot_batch_trade(self, exchange, base_coin, quote_coin, tradeType, prices, amounts, types):

            ex_qt = SpotBatchTrade()
            orders_data = ex_qt.get_orders_data(exchange, base_coin, quote_coin, prices, amounts, types)
            print(orders_data)
            tk = ex_qt.get_spot_batch_trade_result(exchange, base_coin, quote_coin, tradeType, orders_data)

            return tk


        def get_spot_batch_trade_result(self, exchange, base_coin, quote_coin, tradeType, orders_data):
            '''
            # Response
            {'result': True, 'order_info': [{'order_id': 624996965}, {'order_id': 624996968}, {'order_id': 624996970}, {'order_id': 624996972}, {'order_id': 624996975}]}
            '''
            trade = Trade()
            ex_qt = SpotBatchTrade()
            msg = ex_qt.post_trade(exchange, base_coin, quote_coin,tradeType,orders_data)
            trade.Result = msg['result']    #'result': True

            #trade.Trade_id = msg['order_id']
            trade.Time = datetime.now().strftime("%Y%m%d %H:%M:%S.%f")

            return trade


        @classmethod
        def post_trade(cls, exchange, base_coin, quote_coin, tradeType, orders_data):
            # 组合symbol值
            symbol = ut.get_symbol(exchange, base_coin, quote_coin)
            msg = ''
            #    def batchTrade(self, symbol, tradeType, orders_data):
            if ut.okex_exchange.lower() == exchange.lower():
                msg = okexcoinSpot.batchTrade(symbol, tradeType, orders_data)
                print(msg)
                # {'result': True, 'order_info': [{'order_id': 624996965}, {'order_id': 624996968}, {'order_id': 624996970}, {'order_id': 624996972}, {'order_id': 624996975}]}
            else:
                print('no support exchange')

            return msg

        @classmethod
        def get_orders_data(self, exchange, base_coin, quote_coin, prices, amounts, types):
            str_orders_data = ''
            len_i = min(len(prices), len(amounts), len(types))
            #len_i = min(ut.MAX_BATCH_NUM_OKEX, len_i)
            if len_i == 0:
                return str_orders_data
            str_orders_data = '['
            get_data_num = 0
            for i in range(0, len_i):
                #判断价格是否正确
                s_t_rule = spot_trade_rule.SpotTradeRule()
                if get_data_num < ut.MAX_BATCH_NUM_OKEX and s_t_rule.if_right_price(exchange, base_coin, quote_coin, types[i], prices[i]) :
                    str_orders_data += '{price:%f,amount:%f,type:\'%s\'}' % (prices[i], amounts[i], types[i])
                    get_data_num = get_data_num + 1
            str_orders_data += ']'
            return str_orders_data

if __name__ == '__main__':
    ex_qt = SpotBatchTrade()
    exchange_name = 'okex'
    base_coin = 'eos'
    quote_coin = 'usdt'
    tradeType = 'sell'
    orders_data = ''
    tk = ex_qt.get_spot_batch_trade_result(exchange_name, base_coin, quote_coin, tradeType, orders_data)
    print('result:%s' %tk.Result + ',trade_id:%s' %tk.Trade_id)
