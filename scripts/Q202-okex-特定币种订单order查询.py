#!/usr/bin/env python

import talang.trader.query.spot_order_query as spot_order_q


def main():

    ex_qt = spot_order_q.spot_order_query()
    exchange_name = 'okex'
    base_coin = 'eos'
    quote_coin = 'usdt'
    order_id = -1#"480894458"
    orders = ex_qt.get_orders_value(exchange_name, base_coin, quote_coin,order_id)
    orders.print_detail()


if __name__ == "__main__":
    main()