#!/usr/bin/env python

import talang.data.quote.quote_symbols as symbol_api
from talang.util.model.Symbol import Symbols


def main():
    ex_qt = symbol_api.QuoteSymbols()
    exchange_name = 'okex'
    sybs = ex_qt.get_basecoinsymbols_by_quote_coin(exchange_name, 'btc')
    sybs.print_detail()

    #samebasecoin = ex_qt.get_samebasecoin_of_diff_quote_coin(exchange_name, 'eth', 'btc')
    #print(samebasecoin)
    #print(len(samebasecoin))

if __name__ == "__main__":
    main()
