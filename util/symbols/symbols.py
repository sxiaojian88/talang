import talang.util.util_data as talang_util

"""
定价币种(quote_coin):usdt,btc,eth;此外okex有bch,zb有qc，暂不考虑
基础币种(base_coin):btc,eth,bch,eos,xrp,ltc......
交易站点(exchange_name):huobipro,okex,zb....
"""

def format_symbol(base_coin,quote_coin,exchange_name):
    
    quotecoin=quote_coin.lower()
    basecoin=base_coin.lower()
    exchange=exchange_name.lower()
    
    if quotecoin not in talang_util.support_quotecoin:
        return "err:quotecoin is not supported"
    if exchange not in talang_util.support_exchange:
        return "err:exchanges is not supported"
    if basecoin == quotecoin or base_coin=="usdt":
        return "err:not right trade coin pair "
    
    if exchange == "huobipro" or exchange == "huobi":
        return basecoin+quotecoin
    else :
        return basecoin+"_"+quotecoin
