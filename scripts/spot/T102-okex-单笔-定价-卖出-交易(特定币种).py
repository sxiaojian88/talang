#!/usr/bin/env python

import talang.trader.trade.spot_trade as spot_trad_api
from talang.util.model.Trade import Trade


def main():

    #T102-okex-单笔-定价-卖出-交易(特定币种)
    #===============输入参数=======================
    base_coin = 'xrp'
    quote_coin = 'usdt'
    price = 5
    amount = 1
    # =============================================
    ex_qt = spot_trad_api.SpotTrade()
    exchange_name = 'okex'
    tradeType = 'sell'

    #买卖价格校验，买价不能比卖价高，卖价不能比买价低

    tk = ex_qt.get_spot_trade_result(exchange_name, base_coin, quote_coin, tradeType, price, amount)
    print('result:%s' %tk.Result + ',trade_id:%s' %tk.Trade_id)

if __name__ == "__main__":
    main()
