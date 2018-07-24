#!/usr/bin/env python

import talang.data.quote.quote_depth as depth_api


def main():

    ex_qt = depth_api.QuoteDepth()
    exchange_name = 'okex'
    base_coin = 'eos'
    quote_coin = 'usdt'

    buy1, sell1, buy1_volume, sell1_volume = ex_qt.get_buy1_and_sell1(exchange_name, base_coin, quote_coin)
    print("buy1:%f,sell1:%f,buy1_volume:%f,sell1_volume:%f" %(buy1, sell1,buy1_volume,sell1_volume))

if __name__ == "__main__":
    main()
