#!/usr/bin/env python

import talang.data.quote.quote_symbols as symbol_api
from talang.util.model.Order import Orders
import talang.trader.query.spot_order_query as spot_order_q
import time
from datetime import datetime


import collections
import concurrent.futures
import math
import multiprocessing

Result = collections.namedtuple("Result", "name")
Summary = collections.namedtuple("Summary", "todo canceled")
orders_total = Orders()


def main():

    #目前不够稳定
    #===============输入参数=======================
    # 无
    # =============================================

    exchange_name = 'okex'
    ex_qs = symbol_api.QuoteSymbols()
    sybs = ex_qs.get_all_symbols(exchange_name)
    #sybs.print_detail()
    concurrency = 2   #并发数量
    print('begin:%s' % datetime.now().strftime("%Y%m%d %H:%M:%S.%f"))

    do_work(sybs, concurrency)

    orders_total.print_detail()
    print('end:%s' % datetime.now().strftime("%Y%m%d %H:%M:%S.%f"))


def do_work(symbols, concurrency):
    futures = set()
    with concurrent.futures.ProcessPoolExecutor(
            max_workers=concurrency) as executor:
        for syb in symbols.symbols_list:
            future = executor.submit(get_orders_value, syb.exchange, syb.base_coin, syb.quote_coin)
            futures.add(future)
            time.sleep(0.1)

        summary = wait_for(futures)
        if summary.canceled:
            executor.shutdown()
    return summary


def get_orders_value(exchange_name, base_coin, quote_coin):
    ex_qt = spot_order_q.spot_order_query()
    order_id = -1
    orders = ex_qt.get_orders_value(exchange_name, base_coin, quote_coin, order_id)
    #print("get_orders_value:" + base_coin + quote_coin)
    #orders.print_detail()
    return orders


def wait_for(futures):
    canceled = False
    try:
        for future in concurrent.futures.as_completed(futures):
            err = future.exception()
            if err is None:
                orders = future.result()
                orders_total.add_orders(orders)
                #if len(orders.Orders_list) > 0:
                    #print('wait_for...e:%d' % len(orders.Orders_list))
                #Qtrac.report("{} {}".format("copied" if result.copied else
                #                            "scaled", os.path.basename(result.name)))
            #elif isinstance(err, Image.Error):
                #Qtrac.report(str(err), True)
            #else:
            #    raise err  # Unanticipated
    except KeyboardInterrupt:
        #Qtrac.report("canceling...")
        canceled = True
        for future in futures:
            future.cancel()
    return Summary(len(futures), canceled)


    #总任务索引列表

    #总结果列表

    #并发进程/线程数量

    #每项任务处理规模

'''
将总任务进行切分
总任务清单索引：symbols_list
每份任务的规模：
'''
def jobs_split(symbols_list_total,sizes):

    return ''
'''
将切分后的子任务加到总任务列表中
子任务：
'''
def add_jobs(symbols_list_son):

    return ''

'''
将切分后的子任务加到总任务列表中
子任务：
'''
def do_one(symbols_list_son):

    return ''

if __name__ == "__main__":
    main()
