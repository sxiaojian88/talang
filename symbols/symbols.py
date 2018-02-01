import talang.util.util_data as talang_util

"""
交易币种(tradecoin):btc,eth,bch,eos,xrp,ltc......
基准币种(basecoin):usdt,btc,eth;此外okex有bch,zb有qc，暂不考虑
交易站点(exchanges):huobipro,okex,zb....
"""

def get_trade_symbol(tradecoin,basecoin,exchange):
    
    tradecoin=tradecoin.lower()
    basecoin=basecoin.lower()
    exchange=exchange.lower()
    
    if basecoin not in talang_util.support_basecoin:
        return "err:basecoin is not supported"
    if exchange not in talang_util.support_exchange:
        return "err:exchanges is not supported"
    if basecoin == tradecoin or tradecoin=="usdt":
        return "err:not right trade coin pair "
    
    if exchange == "huobipro" :
        return tradecoin+basecoin
    else :
        return tradecoin+"_"+basecoin
