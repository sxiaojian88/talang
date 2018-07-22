#!/usr/bin/env python
import talang.util.util_data as ut
import talang.trader.trade.spot_trade_cancel as spot_trad_cancel_api


def main():

    ex_qt = spot_trad_cancel_api.SpotTradeCancel()
    exchange_name = 'okex'
    base_coin = 'eos'
    quote_coin = 'usdt'
    order_id = '637839142'
    symbol = ut.get_symbol(exchange_name, base_coin, quote_coin)
    tk = ex_qt.get_spot_trade_cancel_result(exchange_name, symbol, order_id)
    print('result:%s' %tk.Result + 'trade_id:%s' %tk.Trade_id)

if __name__ == "__main__":
    main()
