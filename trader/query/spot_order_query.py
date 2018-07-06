# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util
import talang.util.util_data as ut
from datetime import datetime
from talang.util.model.Order import Order
from talang.util.model.Order import Orders
# 现货API
okexcoinSpot = okex_util.getOkcoinSpot()
# 期货API
okexcoinFuture = okex_util.getOkcoinFuture()


class spot_order_query():

        def get_orders_value(self, exchange, base_coin, quote_coin, order_id):
            orders = Orders()
            spot_oder_q = spot_order_query()
            msg = spot_oder_q.get_msg(exchange, base_coin, quote_coin, order_id)

            if msg['result'] is not True:
                return orders

            result_true = msg['orders']
            #print(result_msg)
            for i in range(len(result_true)):
                order = Order()
                result_order = result_true[i]
                #print(result_msg)
                order.Amount = float(result_order['amount'])
                #print(order.Amount)
                order.Avg_price = float(result_order['avg_price'])
                create_date = float(result_order["create_date"])/1000
                #print(create_date)
                order.Create_date = datetime.fromtimestamp(create_date).strftime("%Y%m%d %H:%M:%S")
                order.Deal_amount = float(result_order['deal_amount'])
                order.Order_id = result_order["order_id"]
                order.Orders_id = result_order["orders_id"]
                order.Price = float(result_order["price"])
                order.Status = result_order["status"]
                order.Symbol = result_order["symbol"]
                order.Type = result_order["type"]
                order.Exchange = ut.okex_exchange
                orders.add_order(order)
            orders.sort_order()
            return orders


        @classmethod
        def get_msg(cls, exchange, base_coin, quote_coin, order_id):
            # 组合symbol值
            symbol = ut.get_symbol(exchange, base_coin, quote_coin)
            msg = ''
            if ut.okex_exchange.lower() == exchange.lower():
                msg = okexcoinSpot.orderInfo(symbol, order_id)
                #print(msg)
                #{'result': True, 'orders': [{'amount': 1, 'avg_price': 0, 'create_date': 1530020990000, 'deal_amount': 0, 'order_id': 480894458, 'orders_id': 480894458, 'price': 108, 'status': 0, 'symbol': 'EOS_USDT', 'type': 'sell'}]}
            else:
                print('no support exchange')


            return msg

if __name__ == '__main__':
    ex_qt = spot_order_query()
    exchange_name = 'okex'
    base_coin = 'eos'
    quote_coin = 'usdt'
    order_id = -1#"480894458"
    orders = Orders()
    orders=ex_qt.get_orders_value(exchange_name, base_coin, quote_coin,order_id)
    orders.print_detail()

    #tk = ex_qt.get_tiker_value(exchange_name, base_coin, quote_coin)
    #print("date:%s" %tk.Time+",high:%f" %tk.High + ",vol:%f" %tk.Volume \
    #      + ",last:%f" %tk.Last + ",low:%f" %tk.Low + ",buy:%f" %tk.Buy + ",sell:%f" %tk.Sell)