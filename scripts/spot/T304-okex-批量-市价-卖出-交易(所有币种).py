#!/usr/bin/env python

import talang.trader.trade.spot_trade as spot_trad_api
import talang.manage.account.spot_account_service as act_api

def main():

    #T304-okex-批量-市价-卖出-交易(所有币种)
    #==================输入参数===========================
    per = 0.01          #卖出所有资产（free）的百分比，0.1表示10%
    quote_coin = 'usdt' #换回的币种
    #=====================================================

    ex_qt = spot_trad_api.SpotTrade()
    exchange_name = 'okex'
    trade_type = 'sell_market'
    price = 0

    #获取币币交易账户信息
    act = act_api.AccountSpotService()
    okex_account = act.get_account_okex()

    for balance in okex_account.balances:
        base_coin = balance.currency
        amount = balance.free * per
        tk = ex_qt.get_spot_trade_result(exchange_name, base_coin, quote_coin, trade_type, price, amount)
        print('base_coin:%s,amount:%f,result:%s,trade_id:%s' % (base_coin, amount, tk.Result, tk.Trade_id))

if __name__ == "__main__":
    main()
