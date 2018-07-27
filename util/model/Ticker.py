from datetime import datetime
import talang.util.util_data as ut

'''
市场行情 由GetTicker函数返回
{
    High    :最高价
    Low     :最低价
    Sell    :卖一价
    Buy     :买一价
    Last    :最后成交价
    Volume  :最近成交量
}
'''


class Ticker:
    """
    Trade. Container of date, time, trade price, volume and side.
    """
    def __init__(self):
        """
        Constructor
        :param exch: Exchange name
        :param instmt: Instrument name
        :param default_format: Default date time format
        """
        self.Exchange = ut.okex_exchange
        self.Symbol = ''
        self.Time = datetime(2000, 1, 1, 0, 0, 0).strftime("%Y%m%d %H:%M:%S.%f")
        self.Ticker_id = '0'
        self.High = 0.0
        self.Low = 0.0
        self.Sell = 0.0
        self.Buy = 0.
        self.Last = 0.0
        self.Volume = 0.0
        self.Volume_to_value = 0.0  # Volume_to_value = Last * Volume

    @staticmethod
    def columns():
        """
        Return static columns names
        """
        return ['symbol', 'time', 'ticker_id', 'high', 'low', 'sell', 'buy', 'last', 'volume', 'volume_to_value']

    @staticmethod
    def types():
        """
        Return static column types
        """
        return ['varchar(25)', 'varchar(25)', 'text', 'decimal(20,8)', 'decimal(20,8)', 'decimal(20,8)',
                'decimal(20,8)', 'decimal(20,8)', 'decimal(20,8)', 'decimal(20,8)']

    def values(self):
        """
        Return values in a list
        """
        return [self.Symbol] + [self.Time] + [self.Ticker_id] + \
               [self.High] + [self.Low] + [self.Sell] + [self.Buy] + [self.Last] + [self.Volume] + \
               [self.Volume_to_value]

    def cal_value(self, usdt_value=1):
        self.Volume_to_value = self.Volume * self.Last * usdt_value

    def print_detail(self):
        total_with = 10*15
        print('=' * (total_with))

        format_tile = "%-10s%20s" \
                      "%15s%15s%15s%15s%15s%20s%20s"
        print(format_tile % ("Symbol", "Time",
                             "High", "Low", "Sell", "Buy", "Last", "Volume", "Value(ustd)"))
        print('-' * total_with)
        format_value = "%-10s%20s" \
                       "%15.8f%15.8f%15.8f%15.8f%15.8f%20.4f%20.4f"

        print(format_value % (self.Symbol, self.Time,
                              self.High, self.Low, self.Sell, self.Buy, self.Last, self.Volume, self.Volume_to_value))

        print('=' * total_with)


class Tickers:
    def __init__(self):
        self.Tickers_list = []

    def add_ticker(self, ticker):
        self.Tickers_list.append(ticker)

    def sort_tickers_by_symbol(self):
        self.Tickers_list.sort(key=lambda x: x.Symbol, reverse=True)

    def sort_tickers_by_value(self):
        self.Tickers_list.sort(key=lambda x: x.Volume_to_value, reverse=True)

    def sort_tickers_by_volume(self):
        self.Tickers_list.sort(key=lambda x: x.Volume, reverse=True)

    def print_detail(self):
        total_with = 10*15
        print('=' * total_with)
        format_tile = "%-5s%-10s%20s" \
                      "%15s%15s%15s%15s%15s%20s%20s"
        print(format_tile % ("No.", "Symbol", "Time",
                             "High", "Low", "Sell", "Buy", "Last", "Volume", "Value(usdt)"))
        print('-' * total_with)
        format_value = "%-5d%-10s%20s" \
                       "%15.8f%15.8f%15.8f%15.8f%15.8f%20.4f%20.4f"
        i = 1
        for ticker in self.Tickers_list:
            print(format_value % (i, ticker.Symbol, ticker.Time,
                                  ticker.High, ticker.Low, ticker.Sell, ticker.Buy, ticker.Last, ticker.Volume,
                                  ticker.Volume_to_value))
            i = i+1
        print('=' * total_with)