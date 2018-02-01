#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import accountConfig
from talang.exchanges.okex.okcoinFutureAPI import OKCoinFuture
from talang.exchanges.okex.okcoinSpotAPI import OKCoinSpot

import talang_config.config_data as talang_config

# 初始化ACCESS_KEY, SECRET_KEY, SERVICE_API
ACCESS_KEY = talang_config.OX["USD_1"]["ACCESS_KEY"]
SECRET_KEY = talang_config.OX["USD_1"]["SECRET_KEY"]
SERVICE_API = "https://www.okex.com"#talang_config.OKEX["USD_1"]["SERVICE_API"]


# 现货API
def getOkcoinSpot():
    return OKCoinSpot(SERVICE_API, ACCESS_KEY, SECRET_KEY)


# 期货API
def getOkcoinFuture():
    return OKCoinFuture(SERVICE_API, ACCESS_KEY, SECRET_KEY)
