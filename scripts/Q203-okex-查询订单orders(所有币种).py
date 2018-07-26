#!/usr/bin/env python

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

    exchange_name = 'okex'
    ex_qs = symbol_api.QuoteSymbols()
    #----------------old查询所有symb------------------
    #sybs = ex_qs.get_all_symbols(exchange_name)
    #----------------------------------------------
    #查询账号中冻结的coins，再根据冻结的coins查询相关symbols
    act = act_api.AccountApi()
    coins = act.get_okex_freezed_coins()
    sybs = ex_qs.get_symbols_by_coins(exchange_name, coins)

    print(len(sybs.symbols_list))

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

if __name__ == "__main__":
    main()
