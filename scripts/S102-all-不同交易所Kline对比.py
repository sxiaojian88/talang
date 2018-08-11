# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util
import talang.util.util_data as ut
from talang.util.model.Kline import Kline
from datetime import datetime
import matplotlib.pyplot as plt
import talang.data.quote.quote_kline as quote_kline_okex
import talang.data.quote.quote_kline_zb as quote_kline_zb


def main():
    ex_qk_okex = quote_kline_okex.QuoteKline()
    ex_qk_zb = quote_kline_zb.QuoteKlineZb()

    base_coin = 'eos'
    quote_coin = 'usdt'
    type = '1min'
    size = '1000'
    kl_okex = ex_qk_okex.get_kline_value(ut.okex_exchange, base_coin, quote_coin, type, size)
    kl_zb = ex_qk_zb.get_kline_value(ut.zb_exchange, base_coin, quote_coin, type, size)

    print_two_kline_close(kl_okex, kl_zb)

    plot_two_kline(kl_okex.Close, kl_zb.Close)

def plot_two_kline(kline_one_close, kline_two_close, axs=None):
    drawer = plt if axs is None else axs
    drawer.plot(kline_one_close, c='r')
    drawer.plot(kline_two_close, c='g')
    drawer.grid(True)
    plt.title('kline price')
    plt.xlabel('time')
    plt.ylabel('price')
    plt.show()

def print_two_kline_close(kline_a, kline_b,):

    total_with = 10 + (20 + 15)*2
    print('=' * (total_with))

    format_tile = "%-10s%20s%15s%20s%15s"
    print(format_tile % ("Symbol", "Time(a)", "Close(a)", "Time(b)", "Close(b)"))
    print('-' * total_with)
    format_value = "%-10s%20s%15.8f%20s%15.8f"

    lenm = min(len(kline_a.Symbol), len(kline_b.Symbol))
    for i in range(0, lenm):
        timestampa = float(kline_a.Time[i] / 1000)
        timestampb = float(kline_b.Time[i] / 1000)
        print(format_value % (kline_a.Symbol[i],
                              datetime.fromtimestamp(timestampa).strftime("%Y%m%d %H:%M:%S"), kline_a.Close[i],
                              datetime.fromtimestamp(timestampb).strftime("%Y%m%d %H:%M:%S"), kline_b.Close[i]))

    print('=' * total_with)


if __name__ == "__main__":
    main()
