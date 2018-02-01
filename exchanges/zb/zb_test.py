#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-16 15:29:19
# @Author  : Ryan (tech@huobi.com)
# @Link    : https://www.huobi.com
# @Version : $Id$

import talang.exchanges.zb.zb_api_data as zb_data
import talang.exchanges.zb.zb_api_trade as zb_trade

if __name__ == '__main__':
    # print("获取1分钟线")
    # print(HuobiServices.get_kline('ethcny', '1min'))
    # print("获取合并深度为1的盘口")
    # print(HuobiServices.get_depth('ethcny', 'step1'))
    # print("获取Trade Detail")
    # print(HuobiServices.get_trade('ethcny'))
    # print("获取 Market Detail 24小时成交量数据")
    # print(HuobiServices.get_detail('ethcny'))
    # print("获取支持交易对")
    # print(HuobiServices.get_symbols())
    
    print("获取账户")
    print(zb_trade.zb_api_trade.get_account_info(zb_trade.zb_api_trade()))
    print("获取当前行情")
    print(zb_data.zb_api_data("btc_usdt").ticker())
    # print('下单')
    # print(HuobiServices.orders(0.01, 'api', 'ethcny', 'buy-limit', 1000))
    # print('执行订单')
    # print(HuobiServices.place_order('206418'))
    # print('撤销订单')
    # print(HuobiServices.cancel_order('206418'))
    # print('查询某个订单')
    # print(HuobiServices.order_info('206418'))
    # print('查询某个订单的成交明细')
    # print(HuobiServices.order_matchresults('206418'))
    # print('查询当前委托、历史委托')
    # print(HuobiServices.orders_list('ethcny', 'submitted'))
    # print('查询当前成交、历史成交')
    # print(HuobiServices.orders_matchresults('ethcny'))
    # print('查询虚拟币提币地址')
    # print(HuobiServices.get_withdraw_address('eth'))
    #print('新提币接口')
    #print(HuobiServices.withdraw_new_create('', 0.01, 'btc', 0.0015))


