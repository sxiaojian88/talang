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


class Kline:
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
        self.Exchange = [] #ut.okex_exchange
        self.Symbol = []
        self.Time = []  #datetime(2000, 1, 1, 0, 0, 0).strftime("%Y%m%d %H:%M:%S.%f")
        self.Kline_id = []
        self.Open = []
        self.High = []
        self.Low = []
        self.Close = []
        self.Volume = []
        self.Volume_to_value = []  # Volume_to_value = Last * Volume

    @staticmethod
    def tablename():
        return 'kline'

    @staticmethod
    def columns():
        """
        Return static columns names
        """
        return ['exchange', 'symbol', 'time', 'kline_id', 'open', 'high', 'low',  'close', 'volume', 'volume_to_value']

    @staticmethod
    def types():
        """
        Return static column types
        """
        return ['varchar(25)', 'varchar(25)', 'text', 'decimal(20,8)', 'decimal(20,8)', 'decimal(20,8)',
                'decimal(20,8)',  'decimal(20,8)', 'decimal(20,8)']

    def values(self):
        """
        Return values in a list
        """
        return [self.Exchange] + [self.Symbol] + [self.Time] + [self.Ticker_id] + \
               [self.Open] + [self.High] + [self.Low] + [self.Close] + [self.Volume] + \
               [self.Volume_to_value]

    def cal_value(self, usdt_value=1):
        self.Volume_to_value = self.Volume * self.Last * usdt_value

    def print_detail(self):
        total_with = 10*15
        print('=' * (total_with))

        format_tile = "%-10s%20s" \
                      "%15s%15s%15s%15s%20s%20s"
        print(format_tile % ("Symbol", "Time",
                             "Open", "High", "Low",  "Close",  "Volume", "Value(ustd)"))
        print('-' * total_with)
        format_value = "%-10s%20s" \
                       "%15.8f%15.8f%15.8f%15.8f%20.4f%20.4f"
        for i in range(0, len(self.Symbol)):
            timestamp = float(self.Time[i]/1000)
            print(format_value % (self.Symbol[i], datetime.fromtimestamp(timestamp).strftime("%Y%m%d %H:%M:%S"),
                                  self.Open[i], self.High[i], self.Low[i], self.Close[i], self.Volume[i], self.Volume_to_value[i]))

        print('=' * total_with)
