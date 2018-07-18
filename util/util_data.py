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

#美元汇率
USDT_CNY=6.45

MAX_BATCH_NUM_OKEX = 5

def get_symbol(exchange, base_coin, quote_coin):
    # 组合symbol值
    if okex_exchange.lower() == exchange.lower():
        topic = base_coin.upper() + '_' + quote_coin.upper()
    else:
        topic = base_coin.upper() + quote_coin.upper()
    return topic

def get_base_coin(exchange,symbol):
    bc = ''
    if okex_exchange.lower() == exchange.lower() and len(symbol) > 0:
        s = symbol.split('_')
        bc = s[0]
    else:
        bc = ''

    return bc

def get_quote_coin(exchange,symbol):
    qc = ''
    if okex_exchange.lower() == exchange.lower() and len(symbol) > 0:
        s = symbol.split('_')
        qc = s[1]
    else:
        qc = ''

    return qc