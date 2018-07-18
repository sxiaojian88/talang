# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util
import talang.util.util_data as ut
from talang.util.model.Ticker import Ticker
from datetime import datetime

# 现货API
okexcoinSpot = okex_util.getOkcoinSpot()
# 期货API
okexcoinFuture = okex_util.getOkcoinFuture()


class QuoteTicker():

        def get_tiker_value(self, exchange, base_coin, quote_coin):
            ticker = Ticker()
            ex_qt = QuoteTicker()
            msg = ex_qt.get_msg(exchange, base_coin, quote_coin)
            # Date time
            timestamp = float(msg["date"])
            ticker.Time= datetime.fromtimestamp(timestamp).strftime("%Y%m%d %H:%M:%S")
            msg = msg["ticker"]
            ticker.Buy = float(msg['buy'])
            ticker.High = float(msg['high'])
            ticker.Last = float(msg['last'])
            ticker.Low = float(msg['low'])
            ticker.Sell = float(msg['sell'])
            ticker.Volume = float(msg['vol'])
            ticker.Symbol = ut.get_symbol(exchange, base_coin, quote_coin)
            ticker.cal_value()
            return ticker


        @classmethod
        def get_msg(cls, exchange, base_coin, quote_coin):
            # 组合symbol值
            symbol = ut.get_symbol(exchange, base_coin, quote_coin)
            msg = ''
            if ut.okex_exchange.lower() == exchange.lower():
                msg = okexcoinSpot.ticker(symbol)
                #print(msg)
                #{'date': '1529836574', 'ticker': {'high': '6256.6379', 'vol': '28947.4171', 'last': '5861.3241', 'low': '5782.2121', 'buy': '5861.6735', 'sell': '5864.9063'}}
            else:
                print('no support exchange')

            return msg


if __name__ == '__main__':
    ex_qt = QuoteTicker()
    exchange_name = 'okex'
    base_coin = 'eos'
    quote_coin = 'usdt'
    tk = Ticker()
    tk = ex_qt.get_tiker_value(exchange_name, base_coin, quote_coin)
    tk.print_detail()