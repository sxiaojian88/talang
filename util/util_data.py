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
#zb exchange名
zb_exchange = "zb"

#美元汇率
USDT_CNY=6.8
#okex批量spot交易每次最大可送的值（okex限制）
MAX_BATCH_NUM_OKEX = 5

#交易所返回kline的最大条数
MAX_KLINE_SIZE_OKEX = 2000  #okex最大返回2000
MAX_KLINE_SIZE_ZB = 1000    #zb最大返回1000

#rest API请求失败时，重试次数
RE_TRY_TIMES = 10
#三角套利方向
RIGHT_DIRECT = 'right'
LEFT_DIRECT = 'left'

#okex合约支持币种对
OKEX_FUTURE_SYMBOLS = ["btc_usd", "ltc_usd", "eth_usd", "etc_usd", "bch_usd", "btg_usd", "xrp_usd", "eos_usd"]
#okex合约执行的期限类别
OKEX_FUTURE_CONTRACT_TYPES= ["this_week", "next_week", "quarter"]
#okex合约多仓方向
OKEX_LONG = 'LONG'
#okex合约空仓方向
OKEX_SHORT = 'SHORT'
#okex合约未知
OKEX_NA = 'NA'
#okex完成状态
OKEX_YES = 'YES'
#okex未完成状态
OKEX_NO = 'NO'
#SQLPLITE数据库保存的地址
SQLPLITE_PATH = "D:\\sqlite_files\\talang.database"


def get_symbol(exchange, base_coin, quote_coin):
    # 组合symbol值
    if okex_exchange.lower() == exchange.lower():
        topic = str.lower(base_coin) + '_' + str.lower(quote_coin)
    else:
        topic = str.lower(base_coin) + str.lower(quote_coin)
    return topic

def get_base_coin(exchange,symbol):
    bc = ''
    if okex_exchange.lower() == exchange.lower() and len(symbol) > 0:
        s = symbol.split('_')
        bc = str.lower(s[0])
    else:
        bc = ''

    return bc

def get_quote_coin(exchange,symbol):
    qc = ''
    if okex_exchange.lower() == exchange.lower() and len(symbol) > 0:
        s = symbol.split('_')
        qc = str.lower(s[1])
    else:
        qc = ''

    return qc