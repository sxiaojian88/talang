#!/usr/bin/env python

import talang.data.quote.quote_symbols as symbol_api
from talang.util.model.Symbol import Symbols


def main():
    ex_qt = symbol_api.QuoteSymbols()
    exchange_name = 'okex'
    sybs = ex_qt.get_all_symbols(exchange_name)
    sybs.print_detail()


if __name__ == "__main__":
    main()
