#!/usr/bin/env python

import talang.data.quote.quote_tickers as tickers_api


def main():

    ex_qt = tickers_api.QuoteTickers()
    exchange_name = 'okex'
    tks = ex_qt.get_tikers_value(exchange_name)
    tks.cal_value()
    tks.sort_tickers_by_value()
    #tks.sort_tickers_by_volume()
    tks.print_detail()


if __name__ == "__main__":
    main()
