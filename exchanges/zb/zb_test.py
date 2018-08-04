#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-16 15:29:19
# @Author  : Ryan (tech@huobi.com)
# @Link    : https://www.huobi.com
# @Version : $Id$

import talang.exchanges.zb.zb_api_data as zb_data
import talang.exchanges.zb.zb_api_trade as zb_trade

if __name__ == '__main__':

    print("获取账户")
    print(zb_trade.zb_api_trade.get_account_info(zb_trade.zb_api_trade()))
    print("获取当前行情")
    print(zb_data.zb_api_data("btc_usdt").ticker())
    print("获取当前kline行情")
    print(zb_data.zb_api_data("btc_usdt").kline())


