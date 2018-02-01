# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util

# 现货API
okcoinSpot = okex_util.getOkcoinSpot()

# 期货API
okcoinFuture = okex_util.getOkcoinFuture()

class account():
    """
    {
    'currency': 'QC', 
    'free': '0.00000000'
    'frozen': '0.00000000', 
    'borrow': '0.00000000', 
    'total_btc_value': '0.00000000',
    'total_usdt_value': '0.00000000',
    'total_cny_value': '0.00000000',
    },
    """
    
    def get_account_by_exchange(exchange):
    
        return "ok"
    
    def get_all_symbols_btc_usdt_cny():
        '''
        return as keys:
        {
            "btc":
            {
                "btc":1,
                "usdt":10000,
                "cny":73000,
            },
            "usdt"
            {
                "btc":0.0001,
                "usdt":1,
                "cny":7.3,
            },
            "eth"
            {
                "btc":0.1,
                "usdt":1000,
                "cny":7300,
            },
            ...
        }
        '''
        
        #0.获取currency的keys列表，剔除：usdt,btc
        
        #1.先设定ustd/cny=7.3
        
        #2.获取btc/usdt的值
        
        #3.获取其他币种(sym/usdt）值
            #3.1计算出(sym/btc)值=(sym/usdt)/(btc/usdt)
            #3.2计算出(sym/cny)值=(sym/usdt）*(ustd/cny)
        #4.如获取不到3的(sym/usdt)值，则获取(sym/btc)值
            #4.1计算出(sym/usdt)值=(sym/btc)*(btc/usdt)
            #4.2计算出(sym/cny)值=(sym/usdt）*(ustd/cny)
        
        
        
        
        return "ok"
    
    def get_btc_value_by_symbol(symbol):
        
        return 0
    def get_usdt_value_by_symbol(symbol):
        
        return 0
    
    def get_cny_value_by_symbol(symbol):
        
        return 0
    
    def get_account_huobipro():
    
        return "ok"

    def get_account_okex():
        
        res=okcoinSpot.userInfo()
        info=res["info"]
        funds=info["funds"]
        borrow=funds["borrow"]
        free=funds["free"]
        freezed=funds["freezed"]
        keys = list(free.keys())
        for i in range(0, len(keys)):
            if float(free[keys[i]]) > 0 or float(freezed[keys[i]]) > 0 or float(borrow[keys[i]]) > 0 :
                print("currency:"+keys[i]+",free:"+free[keys[i]]+",frozen:"+freezed[keys[i]]+",borrow:"+borrow[keys[i]])
        return "ok"

    def get_account_zb():
    
        return "ok"


