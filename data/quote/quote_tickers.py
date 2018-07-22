# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util
import talang.util.util_data as ut
from talang.util.model.Ticker import Ticker
from talang.util.model.Ticker import Tickers
from datetime import datetime

# 现货API
okexcoinSpot = okex_util.getOkcoinSpot()
# 期货API
okexcoinFuture = okex_util.getOkcoinFuture()


class QuoteTickers:

        def get_tikers_value(self, exchange):
            tickers = Tickers()
            ex_qt = QuoteTickers()
            msg = ex_qt.get_msg(exchange)
            timestamp = float(msg["date"])
            time_ticker = datetime.fromtimestamp(timestamp).strftime("%Y%m%d %H:%M:%S")

            msg_tickers = msg["tickers"]
            for i in range(len(msg_tickers)):
                ticker = Ticker()
                msg_ticker = msg_tickers[i]
                ticker.Time = time_ticker
                ticker.Buy = float(msg_ticker['buy'])
                ticker.High = float(msg_ticker['high'])
                ticker.Last = float(msg_ticker['last'])
                ticker.Low = float(msg_ticker['low'])
                ticker.Sell = float(msg_ticker['sell'])
                ticker.Volume = float(msg_ticker['vol'])
                ticker.Symbol = msg_ticker['symbol'].lower()
                tickers.add_ticker(ticker)
            #tickers.cal_value()
            return tickers

        @classmethod
        def get_msg(cls, exchange):
            msg = ''
            if ut.okex_exchange.lower() == exchange.lower():
                msg = okexcoinSpot.tickers()
                #print(msg)
                #{'date': '1529836574', 'ticker': {'high': '6256.6379', 'vol': '28947.4171', 'last': '5861.3241', 'low': '5782.2121', 'buy': '5861.6735', 'sell': '5864.9063'}}
            else:
                print('no support exchange')
            return msg


if __name__ == '__main__':
    ex_qt = QuoteTickers()
    exchange_name = 'okex'
    tks = Tickers()
    tks = ex_qt.get_tikers_value(exchange_name)
    tks.sort_tickers_by_value()
    tks.print_detail()