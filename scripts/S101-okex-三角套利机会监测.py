#!/usr/bin/env python

import talang.data.quote.quote_depth as depth_api
import talang.data.quote.quote_symbols as symbol_api
from talang.util.model.Triangle import Triangle
from talang.util.model.Triangle import Triangles
from datetime import datetime


def main():

    #S101-okex-三角套利机会监测
    #===============输入参数=======================
    threshold_value = 0.001 #阈值
    go_times_set = 1          #跑多少次循环
    # =============================================

    print('begin:%s' % datetime.now().strftime("%Y%m%d %H:%M:%S.%f"))
    symbol_qt = symbol_api.QuoteSymbols()

    depth_qt = depth_api.QuoteDepth()
    exchange_name = 'okex'
    #base_coin = 'eos'

    total_with = 6 * 15 + 5 + 18 * 2
    print('=' * total_with)
    format_tile = "%-5s%-10s%20s" \
                  "%15s%15s%15s" \
                  "%18s%18s"
    print(format_tile % ("No.", "Exchange", "Time",
                         "Base_Coin", "Quote_Coin", "Middle_Coin",
                         "Right_direction", "Left_direction"))


    '''
    1:eth,btc,2:btc,usdt,3.eth,usdt,
    4.okb,eth,5,okb,btc,6.okb,usdt
    '''
    coin_pairs = [['eth', 'btc'], ['btc', 'usdt'], ['eth', 'usdt'],
                  ['okb', 'btc'], ['okb', 'eth'], ['okb', 'usdt']]
    tris = Triangles()

    go_times = 0
    while True:
        go_times += 1
        if go_times > go_times_set:
            break
        for pairs in coin_pairs:
            quote_coin = pairs[0]#'btc'
            middle_coin = pairs[1]#'usdt'

            samebasecoin = symbol_qt.get_samebasecoin_of_diff_quote_coin(exchange_name, quote_coin, middle_coin)
            #print(samebasecoin)
            #print(len(samebasecoin))

            i = 1
            for base_coin in samebasecoin:
                tri = Triangle()
                tri.exchange = exchange_name
                tri.quote_coin = quote_coin
                tri.base_coin = base_coin
                tri.middle_coin = middle_coin
                tri.time = datetime.now().strftime("%Y%m%d %H:%M:%S")
                tri.right_direction = 0
                tri.left_direction = 0

                tri.BC_MC_buy_1_price, tri.BC_MC_sell_1_price, tri.BC_MC_buy_1_volume, tri.BC_MC_sell_1_volume = \
                    depth_qt.get_buy1_and_sell1(exchange_name, base_coin, middle_coin)
                tri.QC_MC_buy_1_price, tri.QC_MC_sell_1_price, tri.QC_MC_buy_1_volume, tri.QC_MC_sell_1_volume = \
                    depth_qt.get_buy1_and_sell1(exchange_name, quote_coin, middle_coin)
                tri.BC_QC_buy_1_price, tri.BC_QC_sell_1_price, tri.BC_QC_buy_1_volume, tri.BC_QC_sell_1_volume = \
                    depth_qt.get_buy1_and_sell1(exchange_name, base_coin, quote_coin)

                if tri.QC_MC_sell_1_price * tri.BC_QC_sell_1_price != 0:
                    tri.right_direction = tri.BC_MC_buy_1_price / (tri.QC_MC_sell_1_price * tri.BC_QC_sell_1_price) - 1
                    #print('No.:%d,base_coin:%s,result:%f' % (i,base_coin, tri.right_direction))
                else:
                    print('QC_MC_sell_1_price*BC_QC_sell_1_price:0')

                if tri.QC_MC_buy_1_price * tri.BC_QC_buy_1_price != 0:
                    tri.left_direction = 1 - tri.BC_MC_sell_1_price / (tri.QC_MC_buy_1_price * tri.BC_QC_buy_1_price)
                    #print('No.:%d,base_coin:%s,result:%f' % (i, base_coin, tri.left_direction))
                else:
                    print('QC_MC_buy_1_price*BC_QC_buy_1_price:0')

                if tri.right_direction > threshold_value or tri.left_direction > threshold_value:
                    tris.add_triangle(tri)
                    tri.print_direecton(i)
                    i = i + 1

    tris.print_detail_right_direction()

    print('end:%s' % datetime.now().strftime("%Y%m%d %H:%M:%S.%f"))
if __name__ == "__main__":
    main()
