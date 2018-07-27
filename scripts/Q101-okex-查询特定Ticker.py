#!/usr/bin/env python

import talang.data.quote.quote_ticker as tiker_api
from talang.util.model.Ticker import Ticker


def main():

    #===============输入参数=======================
    base_coin = 'qtum'
    quote_coin = 'eth'
    # =============================================

    ex_qt = tiker_api.QuoteTicker()
    exchange_name = 'okex'
    #tk = Ticker()
    tk = ex_qt.get_tiker_value(exchange_name, base_coin, quote_coin)
    tk.print_detail()

if __name__ == "__main__":
    main()
