#!/usr/bin/env python

import talang.data.quote.quote_tikcer as tiker_api;
from talang.util.model.Ticker import Ticker
def main():

    ex_qt = tiker_api.QuoteTiker()
    exchange_name = 'okex'
    base_coin = 'eos'
    quote_coin = 'usdt'
    #tk = Ticker()
    tk = ex_qt.get_tiker_value(exchange_name, base_coin, quote_coin)
    tk.print_detail()

if __name__ == "__main__":
    main()
