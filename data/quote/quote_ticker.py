# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util
import talang.util.util_data as ut
from talang.util.model.Ticker import Ticker
from datetime import datetime
import talang.exchanges.zb.zb_api_data as zb_data
# 现货API
okexcoinSpot = okex_util.getOkcoinSpot()
# 期货API
okexcoinFuture = okex_util.getOkcoinFuture()


class QuoteTicker:

    def get_cny_value(self, usdtvalue):
        return ut.USDT_CNY * usdtvalue

    def get_btc_value_by_coin(self, exchange, coin):
        ex_qt = QuoteTicker()
        value_btc = 1.0
        if coin.lower() == ut.BTC_COIN.lower():
            return value_btc
        # 其他合法性判断，如symbol的值
        if coin.lower() == ut.USDT_COIN.lower():
            value_usdt = ex_qt.get_buy_value_by_ticker(exchange, ut.BTC_COIN.lower(), coin.lower())
            if value_usdt != 0:
                value_btc = 1 / float(value_usdt)

        else:
            value_btc = ex_qt.get_buy_value_by_ticker(exchange, coin.lower(), ut.BTC_COIN.lower())

        return value_btc

    def get_usdt_value_by_coin(self, exchange, coin):
        ex_qt = QuoteTicker()
        value_usdt = 1.0
        if coin.lower() != ut.USDT_COIN.lower():
            value_usdt = ex_qt.get_buy_value_by_ticker(exchange, coin.lower(), ut.USDT_COIN.lower())

        return value_usdt

    def get_buy_value_by_ticker(self, exchange, base_coin, quote_coin):
        ex_qt = QuoteTicker()
        msg = ex_qt.get_msg(exchange, base_coin, quote_coin)
        msg = msg["ticker"]
        buy_1_price = float(msg['buy'])

        return buy_1_price

    def get_sell_value_by_ticker(self, exchange, base_coin, quote_coin):
        ex_qt = QuoteTicker()
        msg = ex_qt.get_msg(exchange, base_coin, quote_coin)
        msg = msg["ticker"]
        sell_1_price = float(msg['sell'])

        return sell_1_price

    def get_tiker_value(self, exchange, base_coin, quote_coin):
        ticker = Ticker()
        ex_qt = QuoteTicker()
        msg = ex_qt.get_msg(exchange, base_coin, quote_coin)

        # Date time
        timestamp = float(msg["date"])

        if ut.okex_exchange.lower() == exchange.lower():
            ticker.Time = datetime.fromtimestamp(timestamp).strftime("%Y%m%d %H:%M:%S")
        elif ut.zb_exchange.lower() == exchange.lower():
            ticker.Time = datetime.fromtimestamp(timestamp/1000).strftime("%Y%m%d %H:%M:%S")

        msg = msg["ticker"]
        ticker.Buy = float(msg['buy'])
        ticker.High = float(msg['high'])
        ticker.Last = float(msg['last'])
        ticker.Low = float(msg['low'])
        ticker.Sell = float(msg['sell'])
        ticker.Volume = float(msg['vol'])
        ticker.Symbol = ut.get_symbol(exchange, base_coin, quote_coin)
        ticker.Volume_to_value = ticker.Volume * ticker.Last * ex_qt.get_usdt_value_by_coin(exchange, quote_coin)

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
        elif ut.zb_exchange.lower() == exchange.lower():
            msg = zb_data.zb_api_data(symbol).ticker()
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