#!/usr/bin/env python

import talang.data.quote.quote_depth as depth_api
import talang.data.quote.quote_symbols as symbol_api
from talang.util.model.Triangle import Triangle
from talang.util.model.Triangle import Triangles
from datetime import datetime


def main():
    '''
    BC_MC=EOSBTC
    QC_MC=ETHBTC
    BC_QC=EOSETH
    '''
    BC_MC_buy_1_price = 0
    BC_MC_sell_1_price = 0
    QC_MC_buy_1_price = 0
    QC_MC_sell_1_price = 0
    BC_QC_buy_1_price = 0
    BC_QC_sell_1_price = 0

    symbol_qt = symbol_api.QuoteSymbols()

    depth_qt = depth_api.QuoteDepth()
    exchange_name = 'okex'
    #base_coin = 'eos'
    '''
    1:eth,btc,2:btc,usdt,3.eth,usdt,
    4.eth,okb,5,btc,okb,6.usdt,okb
    '''
    quote_coin = 'usdt'
    middle_coin = 'okb'

    samebasecoin = symbol_qt.get_samebasecoin_of_diff_quote_coin(exchange_name, quote_coin, middle_coin)
    #print(samebasecoin)
    #print(len(samebasecoin))
    tris = Triangles()
    i = 1
    for base_coin in samebasecoin:
        tri = Triangle()
        tri.exchange = exchange_name
        tri.quote_coin = quote_coin
        tri.base_coin = base_coin
        tri.middle_coin = middle_coin
        tri.time = datetime.now().strftime("%Y%m%d %H:%M:%S.%f")
        tri.right_direction = 0
        tri.left_direction = 0
        BC_MC_buy_1_price, BC_MC_sell_1_price = depth_qt.get_buy1_and_sell1(exchange_name, base_coin, middle_coin)
        QC_MC_buy_1_price, QC_MC_sell_1_price = depth_qt.get_buy1_and_sell1(exchange_name, quote_coin, middle_coin)
        BC_QC_buy_1_price, BC_QC_sell_1_price = depth_qt.get_buy1_and_sell1(exchange_name, base_coin, quote_coin)

        if QC_MC_sell_1_price * BC_QC_sell_1_price != 0:
            tri.right_direction = BC_MC_buy_1_price / (QC_MC_sell_1_price * BC_QC_sell_1_price) - 1
            #print('No.:%d,base_coin:%s,result:%f' % (i,base_coin, tri.right_direction))
        else:
            print('QC_MC_sell_1_price*BC_QC_sell_1_price:0')

        if QC_MC_buy_1_price * BC_QC_buy_1_price != 0:
            tri.left_direction = 1 - BC_MC_sell_1_price / (QC_MC_buy_1_price * BC_QC_buy_1_price)
            #print('No.:%d,base_coin:%s,result:%f' % (i, base_coin, tri.left_direction))
        else:
            print('QC_MC_buy_1_price*BC_QC_buy_1_price:0')
        tris.add_triangle(tri)
        i = i + 1

    tris.sort_by_right_direction()
    tris.print_detail()

    tris.sort_by_left_direction()
    tris.print_detail()

if __name__ == "__main__":
    main()
