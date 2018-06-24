from datetime import datetime
'''
标准OHLC结构, 用来画K线和指标分析用的，由GetRecords函数返回此结构数组
{
    Time    :一个时间戳, 精确到毫秒，与Javascript的 new Date().getTime() 得到的结果格式一样
    Open    :开盘价
    High    :最高价
    Low     :最低价
    Close   :收盘价
    Volume  :交易量
}
'''


class Record:
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
        self.Record_id = ''
        self.Open = 0.0
        self.High = 0.0
        self.Low = 0.0
        self.Close = 0.0
        self.Volume = 0.0

    @staticmethod
    def columns():
        """
        Return static columns names
        """
        return ['time', 'record_id', 'open', 'high', 'low', 'close', 'volume']

    @staticmethod
    def types():
        """
        Return static column types
        """
        return ['varchar(25)', 'text', 'decimal(20,8)', 'decimal(20,8)', 'decimal(20,8)', \
                'decimal(20,8)', 'decimal(20,8)']

    def values(self):
        """
        Return values in a list
        """
        return [self.Time] + [self.Record_id] + [self.Open] + [self.High] + [self.Low] + \
               [self.Close] + [self.Volume]

