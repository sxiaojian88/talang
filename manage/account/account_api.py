# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util
import talang.data.quote.exchange_quote_api as ex_quote_api
import talang.util.util_data as ut
import talang.util.model.Account as acct

# 现货API
okcoinSpot = okex_util.getOkcoinSpot()
# 期货API
okcoinFuture = okex_util.getOkcoinFuture()


class AccountApi():
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
    
    def get_account_by_exchange(self,exchange):
        return "ok"
    
    def get_all_symbols_btc_usdt_cny(self):
        return "ok"
    
    def get_btc_value_by_coin(self, exchange, coin):
        value_btc = 1.0
        if coin.lower() == ut.BTC_COIN.lower():
            return value_btc
        #其他合法性判断，如symbol的值
        if coin.lower() == ut.USDT_COIN.lower():
            value_usdt = ex_quote_api.ExchangeQuoteApi.get_buy_1_value(self, exchange, ut.BTC_COIN.lower(), coin.lower())
            if value_usdt != 0:
                value_btc = 1/float(value_usdt)

        else:
            value_btc=ex_quote_api.ExchangeQuoteApi.get_buy_1_value(self, exchange, coin.lower(), ut.BTC_COIN.lower())

        return value_btc

    def get_usdt_value_by_coin(self, exchange, coin):
        value_usdt = 1.0
        if coin.lower() != ut.USDT_COIN.lower():
            value_usdt = ex_quote_api.ExchangeQuoteApi.get_buy_1_value(self, exchange, coin.lower(), ut.USDT_COIN.lower())

        return value_usdt
    
    def get_cny_value(self, usdtvalue):
        
        return ut.USDT_CNY*usdtvalue
    
    def get_account_huobipro(self):
    
        return "ok"

    def get_account_okex(self):
        
        res = okcoinSpot.userInfo()
        #print(res)
        info = res["info"]
        funds = info["funds"]
        #borrow = funds["borrow"]
        free = funds["free"]
        freezed = funds["freezed"]
        keys = list(free.keys())
        total_btc = 0.0
        total_usdt = 0.0

        okex_account = acct.SpotAccount()
        okex_account.exchange = ut.okex_exchange

        for i in range(0, len(keys)):
            if float(free[keys[i]]) > 0 or float(freezed[keys[i]]) > 0 :#or float(borrow[keys[i]]) > 0:
                cur = keys[i]
                fre = float(free[keys[i]])
                frd = float(freezed[keys[i]])
                bor = 0#float(borrow[keys[i]])
                total_num = fre+frd+bor
                btc_value = float(self.get_btc_value_by_coin(ut.okex_exchange, cur))
                usdt_value = float(self.get_usdt_value_by_coin(ut.okex_exchange, cur))
                t_btc_value = total_num*btc_value
                t_usdt_value = total_num*usdt_value
                total_btc = total_btc+t_btc_value
                total_usdt = total_usdt+t_usdt_value
                #print("currency:"+cur+",free:%f" % fre+",frozen:%f" % frd+",borrow:%f" % bor +",btc_value:%f" % t_btc_value + ",usdt_value:%f" % t_usdt_value +"(usdt_price:%f)" %usdt_value )

                okex_balance = acct.Balance()
                okex_balance.currency = cur
                okex_balance.free = fre
                okex_balance.frozen = frd
                okex_balance.borrow = bor
                okex_balance.total_num = total_num
                okex_balance.btc_worth = t_btc_value
                okex_balance.btc_price = btc_value
                okex_balance.usdt_worth = t_usdt_value
                okex_balance.usdt_price = usdt_value
                okex_balance.cny_worth = float(self.get_cny_value(t_usdt_value))
                okex_balance.cny_price = float(self.get_cny_value(usdt_value))
                okex_account.add_balance(okex_balance)

        #print("-----------------------------------------------------------------------------")
        #print("total_btc:%f" %total_btc + ",total_usdt:%f" %total_usdt + ",total_cny:%f" %self.get_cny_value(total_usdt) )
        okex_account.total_usdt = total_usdt
        okex_account.total_btc = total_btc
        okex_account.total_cny = self.get_cny_value(total_usdt)
        okex_account.sort_balance()
        okex_account.cal_ccupy()

        return okex_account

    def get_account_zb(self):
    
        return "ok"

    #返回冻结的coin币别
    def get_okex_freezed_coins(self):
        coins = []
        res = okcoinSpot.userInfo()
        # print(res)
        info = res["info"]
        funds = info["funds"]
        freezed = funds["freezed"]
        keys = list(freezed.keys())
        okex_account = acct.SpotAccount()
        okex_account.exchange = ut.okex_exchange

        for i in range(0, len(keys)):
            if  float(freezed[keys[i]]) > 0:
                coins.append(keys[i])

        return coins


if __name__ == "__main__":
    act = AccountApi()
    okex_account = act.get_account_okex()
    okex_account.print_detail()
