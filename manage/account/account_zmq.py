# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util
import talang.data.quote.exchange_quote_zmq as ex_quote
import talang.util.util_data as ut

# 现货API
okcoinSpot = okex_util.getOkcoinSpot()

# 期货API
okcoinFuture = okex_util.getOkcoinFuture()

#美元汇率
USDT_CNY=6.45


class account_zmq():
    def get_account_by_exchange(self,exchange):
        return "ok"
    
    def get_all_symbols_btc_usdt_cny(self):
        return "ok"
    
    def get_btc_value_by_symbol(self, exchange, symbol):
        value_btc = 1.0
        if symbol.lower() == ut.BTC_COIN.lower():
            return value_btc
        #其他合法性判断，如symbol的值
        if symbol.lower() == ut.USDT_COIN.lower():
            value_usdt = ex_quote.exchange_quote_zmq.get_buy_1_value(self, exchange, ut.BTC_COIN.upper(), symbol.upper())
            if value_usdt != 0:
                value_btc = 1/float(value_usdt)

        else:
            value_btc=ex_quote.exchange_quote_zmq.get_buy_1_value(self, exchange, symbol.upper(), ut.BTC_COIN.upper())

        return value_btc

    def get_usdt_value_by_symbol(self,exchange,symbol):
        value_usdt = 1.0
        if symbol.lower() != ut.USDT_COIN.lower():
            value_usdt = ex_quote.exchange_quote_zmq.get_buy_1_value(self, exchange, symbol.upper(), ut.USDT_COIN.upper())

        return value_usdt
    
    def get_cny_value(self, usdtvalue):
        
        return USDT_CNY*usdtvalue
    
    def get_account_huobipro(self):
    
        return "ok"

    def get_account_okex(self):
        
        res=okcoinSpot.userInfo()
        info=res["info"]
        funds=info["funds"]
        borrow=funds["borrow"]
        free=funds["free"]
        freezed=funds["freezed"]
        keys = list(free.keys())
        total_btc=0.0
        total_usdt=0.0

        for i in range(0, len(keys)):
            if float(free[keys[i]]) > 0 or float(freezed[keys[i]]) > 0 or float(borrow[keys[i]]) > 0 :
                cur=keys[i]
                fre=free[keys[i]]
                frd=freezed[keys[i]]
                bor=borrow[keys[i]]
                total_num=float(fre)+float(frd)+float(bor)
                btc_value=float(self.get_btc_value_by_symbol(ut.okex_exchange,cur))
                usdt_value=float(self.get_usdt_value_by_symbol(ut.okex_exchange,cur))
                t_btc_value=total_num*btc_value
                t_usdt_value=total_num*usdt_value
                total_btc=total_btc+t_btc_value
                total_usdt=total_usdt+t_usdt_value
                print("currency:"+cur+",free:"+fre+",frozen:"+frd+",borrow:"+bor+ \
                      ",btc_value:%f" % t_btc_value + ",usdt_value:%f" % t_usdt_value +"(usdt_price:%f)" %usdt_value  )
        print("-----------------------------------------------------------------------------")
        print("total_btc:%f" %total_btc + ",total_usdt:%f" %total_usdt + ",total_cny:%f" %self.get_cny_value(total_usdt) )


        return "ok"

    def get_account_zb(self):
    
        return "ok"


if __name__ == "__main__":
    act=account_zmq()
    act.get_account_okex()

    '''
    btc_value = float(act.get_btc_value_by_symbol(ut.okex_exchange, "BTC"))
    usdt_value = float(act.get_usdt_value_by_symbol(ut.okex_exchange, "BTC"))
    print("btc_btc_quote:%f" % btc_value + \
          ",btc_usdt_quote:%f" % usdt_value)

    btc_value = float(act.get_btc_value_by_symbol(ut.okex_exchange, "USDT"))
    usdt_value = float(act.get_usdt_value_by_symbol(ut.okex_exchange, "USDT"))
    print("USDT_btc_quote:%f" % btc_value + \
          ",USDT_usdt_quote:%f" % usdt_value)
    '''