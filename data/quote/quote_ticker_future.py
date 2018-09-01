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


class QuoteTickerFuture:

    def get_cny_value(self, usdtvalue):
        return ut.USDT_CNY * usdtvalue

    def get_buy_value_by_ticker(self, exchange, base_coin, quote_coin):
        ex_qt = QuoteTickerFuture()
        msg = ex_qt.get_msg(exchange, base_coin, quote_coin)
        msg = msg["ticker"]
        buy_1_price = float(msg['buy'])

        return buy_1_price

    def get_sell_value_by_ticker(self, exchange, base_coin, quote_coin):
        ex_qt = QuoteTickerFuture()
        msg = ex_qt.get_msg(exchange, base_coin, quote_coin)
        msg = msg["ticker"]
        sell_1_price = float(msg['sell'])

        return sell_1_price

    def get_tiker_value(self, exchange, base_coin, quote_coin, contractType = 'this_week'):
        ticker = Ticker()
        ex_qt = QuoteTickerFuture()
        msg = ex_qt.get_msg(exchange, base_coin, quote_coin, contractType)

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
        '''
        "contract_id":20140926012, 
		"unit_amount":100.0
        '''
        ticker.Symbol = ut.get_symbol(exchange, base_coin, quote_coin)
        ticker.Volume_to_value = ticker.Volume * ticker.Last

        return ticker


    @classmethod
    def get_msg(cls, exchange, base_coin, quote_coin, contractType = 'this_week'):
        # symbol值: btc_usd ltc_usd eth_usd etc_usd bch_usd
        #contractType 合约类型: this_week:当周 next_week:下周 quarter:季度
        symbol = ut.get_symbol(exchange, base_coin, quote_coin)
        msg = ''
        if ut.okex_exchange.lower() == exchange.lower():
            msg = okexcoinFuture.future_ticker(symbol, contractType)
            #print(msg)

        elif ut.zb_exchange.lower() == exchange.lower():
            msg = zb_data.zb_api_data(symbol).ticker()
        else:
            print('no support exchange')

        return msg


if __name__ == '__main__':
    ex_qt = QuoteTickerFuture()
    exchange_name = 'okex'
    base_coin = 'btc'
    quote_coin = 'usd'
    tk = Ticker()
    tk = ex_qt.get_tiker_value(exchange_name, base_coin, quote_coin)
    tk.print_detail()