#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import accountConfig
from talang.exchanges.okex.okcoinFutureAPI import OKCoinFuture
from talang.exchanges.okex.okcoinSpotAPI import OKCoinSpot

import talang_config.config_data as talang_config

# 初始化ACCESS_KEY, SECRET_KEY, SERVICE_API
SERVICE_API = "https://www.okex.com"#talang_config.OKEX["USD_1"]["SERVICE_API"]
#主账户
ACCESS_KEY_MAIN = talang_config.OX["USD_1"]["ACCESS_KEY"]
SECRET_KEY_MAIN = talang_config.OX["USD_1"]["SECRET_KEY"]

#子账户TR1
ACCESS_KEY_TR1 = talang_config.OX_TR1["USD_1"]["ACCESS_KEY"]
SECRET_KEY_TR1 = talang_config.OX_TR1["USD_1"]["SECRET_KEY"]





# 现货API
def getOkcoinSpot():
    return OKCoinSpot(SERVICE_API, ACCESS_KEY_MAIN, SECRET_KEY_MAIN)


# 期货API
def getOkcoinFuture():
    return OKCoinFuture(SERVICE_API, ACCESS_KEY_MAIN, SECRET_KEY_MAIN)
