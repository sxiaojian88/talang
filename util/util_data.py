# -*- coding: utf-8 -*-

#系统支持的定价币别，此外okex有bch,zb有qc，暂不考虑
support_quotecoin = ["USDT","BTC","ETH"]
#系统支持的交易站点
support_exchange = ["HuoBiPro","OkEx","Zb"]

USDT_COIN = "USDT"
BTC_COIN = "BTC"
ETH_COIN = "ETH"
#火币exhange名
huobipro_exchange = "HuoBiPro"
#okex exchange名
okex_exchange = "OkEx"



def get_symbol(exchange, base_coin, quote_coin):
    # 组合symbol值
    if okex_exchange.lower() == exchange.lower():
        topic = base_coin.upper() + '_' + quote_coin.upper()
    else:
        topic = base_coin.upper() + quote_coin.upper()
    return topic