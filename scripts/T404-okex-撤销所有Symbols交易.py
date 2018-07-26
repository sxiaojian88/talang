#!/usr/bin/env python
import talang.trader.trade.spot_trade_cancel as spot_trad_cancel_api
import talang.data.quote.quote_symbols as symbol_api
from talang.util.model.Order import Orders
import talang.trader.query.spot_order_query as spot_order_q
import time
from datetime import datetime
import talang.manage.account.account_api as act_api


def main():

    #===============输入参数=======================
    # 无
    # =============================================
    #查询所有Symbols所有orders，参考Q203
    exchange_name = 'okex'
    ex_qs = symbol_api.QuoteSymbols()
    #----------------old查询所有symb------------------
    #sybs = ex_qs.get_all_symbols(exchange_name)
    #----------------------------------------------
    #查询账号中冻结的coins，再根据冻结的coins查询相关symbols
    act = act_api.AccountApi()
    coins = act.get_okex_freezed_coins()
    sybs = ex_qs.get_symbols_by_coins(exchange_name, coins)
    ex_qt = spot_order_q.spot_order_query()
    order_id = -1

    orders_total = Orders()

    print('begin:%s' % datetime.now().strftime("%Y%m%d %H:%M:%S.%f"))

    for syb in sybs.symbols_list:
        orders = ex_qt.get_orders_value(exchange_name, syb.base_coin, syb.quote_coin, order_id)
        orders_total.add_orders(orders)
        time.sleep(0.06)
        #add process....description

    orders_total.print_detail()
    print('end:%s' % datetime.now().strftime("%Y%m%d %H:%M:%S.%f"))

    #逐笔撤销order，程序优化空间：每3笔发一次批量撤销交易，访问频率 20次/2秒控制
    i = 1
    for order in orders_total.Orders_list:
        ex_qt = spot_trad_cancel_api.SpotTradeCancel()
        tk = ex_qt.get_spot_trade_cancel_result(order.Exchange, order.Symbol, order.Order_id)
        print('No.:%d,' %i +'result:%s,' %tk.Result + 'order_id:%s' %tk.Trade_id)
        i = i + 1

if __name__ == "__main__":
    main()
