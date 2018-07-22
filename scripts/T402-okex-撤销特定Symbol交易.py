#!/usr/bin/env python
import talang.trader.query.spot_order_query as spot_order_q
import talang.trader.trade.spot_trade_cancel as spot_trad_cancel_api
import talang.util.util_data as ut


def main():

    #查询特定Symbol所有orders，参考Q202
    ex_qt = spot_order_q.spot_order_query()
    exchange_name = 'okex'
    base_coin = 'xrp'
    quote_coin = 'usdt'
    order_id = -1#"480894458"
    orders = ex_qt.get_orders_value(exchange_name, base_coin, quote_coin,order_id)
    orders.print_detail()

    #逐笔撤销order，程序优化空间：每3笔发一次批量撤销交易，访问频率 20次/2秒控制
    i = 1
    for order in orders.Orders_list:
        ex_qt = spot_trad_cancel_api.SpotTradeCancel()
        tk = ex_qt.get_spot_trade_cancel_result(order.Exchange, order.Symbol, order.Order_id)
        print('No.:%d,' %i +'result:%s,' %tk.Result + 'order_id:%s' %tk.Trade_id)
        i = i + 1

if __name__ == "__main__":
    main()
