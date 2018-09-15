#!/usr/bin/env python

import talang.data.quote.quote_tickers as tickers_api


def main():

    #===============输入参数=======================
    usdt_value_limit = 0   #搜索的最低成交量门槛
    # =============================================

    ex_qt = tickers_api.QuoteTickers()
    exchange_name = 'okex'
    tks = ex_qt.get_tikers_value(exchange_name, usdt_value_limit)
    tks.sort_tickers_by_value()
    #tks.sort_tickers_by_volume()
    tks.print_detail()


if __name__ == "__main__":
    main()
