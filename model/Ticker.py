from datetime import datetime
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
        self.Time = datetime(2000, 1, 1, 0, 0, 0).strftime("%Y%m%d %H:%M:%S.%f")
        self.Ticker_id = ''
        self.High = 0.0
        self.Low = 0.0
        self.Sell = 0.0
        self.Buy = 0.0
        self.Last = 0.0
        self.Volume = 0.0

    @staticmethod
    def columns():
        """
        Return static columns names
        """
        return ['time', 'ticker_id', 'high', 'low', 'sell', 'buy', 'last', 'volume']

    @staticmethod
    def types():
        """
        Return static column types
        """
        return ['varchar(25)', 'text', 'decimal(20,8)', 'decimal(20,8)', 'decimal(20,8)', \
                'decimal(20,8)', 'decimal(20,8)', 'decimal(20,8)']

    def values(self):
        """
        Return values in a list
        """
        return [self.Time] + [self.Ticker_id] + [self.High] + [self.Low] + [self.Sell] + \
               [self.Buy] + [self.Last] + [self.Volume]

