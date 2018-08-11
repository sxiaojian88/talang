# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util
import talang.util.util_data as ut
from talang.util.model.Kline import Kline
from datetime import datetime
import talang.data.quote.quote_ticker as q_ticker
import matplotlib.pyplot as plt

# 现货API
okexcoinSpot = okex_util.getOkcoinSpot()
# 期货API
okexcoinFuture = okex_util.getOkcoinFuture()


class QuoteKline:

    def get_kline_value(self, exchange, base_coin, quote_coin, type='5min', size='1000'):
        qt = q_ticker.QuoteTicker()
        quote_coin_usdt_price = qt.get_usdt_value_by_coin(exchange, quote_coin)

        kline = Kline()
        ex_kl = QuoteKline()
        msg = ex_kl.get_msg(exchange, base_coin, quote_coin, type, size)
        # Date time

        for k in msg:
            kline.Exchange.append(ut.okex_exchange)
            kline.Symbol.append(ut.get_symbol(exchange, base_coin, quote_coin))
            #timestamp = float(k[0]/1000)
            #kline.Time.append(datetime.fromtimestamp(timestamp).strftime("%Y%m%d %H:%M:%S"))
            kline.Time.append(float(k[0]))
            kline.Open.append(float(k[1]))
            kline.High.append(float(k[2]))
            kline.Low.append(float(k[3]))
            kline.Close.append(float(k[4]))
            kline.Volume.append(float(k[5]))
            kline.Volume_to_value.append(float(k[5]) * float(k[4]) * quote_coin_usdt_price)

        return kline


    @classmethod
    def get_msg(cls, exchange, base_coin, quote_coin, type='5min', size='1000'):
        # 组合symbol值
        symbol = ut.get_symbol(exchange, base_coin, quote_coin)
        msg = ''
        if ut.okex_exchange.lower() == exchange.lower():
            msg = okexcoinSpot.kline(symbol, type, size)
            #print(msg)
            #[[1532986200000,"0.01010073","0.01010073","0.01010073","0.01010073","12.7557"],[1532986260000,"0.01010381","0.01010381","0.01009715","0.01009715","24.53925"],
        else:
            print('no support exchange')

        return msg

    def plot_close(self, close, axs=None):
        drawer = plt if axs is None else axs
        drawer.plot(close, c='r')
        drawer.grid(True)
        plt.title('close price')
        plt.xlabel('time')
        plt.ylabel('close')
        plt.show()


if __name__ == '__main__':
    ex_qt = QuoteKline()
    exchange_name = 'okex'
    base_coin = 'eos'
    quote_coin = 'usdt'
    kl = Kline()
    kl = ex_qt.get_kline_value(exchange_name, base_coin, quote_coin)
    kl.print_detail()
    ex_qt.plot_close(kl.Close)