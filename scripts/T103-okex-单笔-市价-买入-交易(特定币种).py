#!/usr/bin/env python

import talang.trader.trade.spot_trade as spot_trad_api
from talang.util.model.Trade import Trade


def main():

    #T103-okex-单笔-市价-买入-交易(特定币种)
    #===============输入参数=======================
    base_coin = 'eos'
    quote_coin = 'usdt'
    price = 1   #买入花销的quote_coin数量
    # =============================================

    ex_qt = spot_trad_api.SpotTrade()
    exchange_name = 'okex'
    tradeType = 'buy_market'
    amount = 0

    #买卖价格校验，买价不能比卖价高，卖价不能比买价低

    tk = ex_qt.get_spot_trade_result(exchange_name, base_coin, quote_coin, tradeType, price, amount)
    print('result:%s' %tk.Result + ',trade_id:%s' %tk.Trade_id)

if __name__ == "__main__":
    main()
