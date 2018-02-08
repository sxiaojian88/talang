from datetime import datetime
from talang.model.MarketOrder import MarketOrder

'''
获取所有交易历史(非自己),由GetTrades函数返回。
{
    Time	:时间(Unix timestamp 毫秒)
    Price	:价格
    Amount	:数量
    Type	:订单类型, 参考常量里的订单类型
}
'''


class Trade:
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
        self.Trade_id = ''
        self.Price = 0.0
        self.Amount = 0.0
        self.Type = MarketOrder.Side.NONE

    @staticmethod
    def columns():
        """
        Return static columns names
        """
        return ['time', 'trade_id', 'price', 'amount', 'type']

    @staticmethod
    def types():
        """
        Return static column types
        """
        return ['varchar(25)', 'text', 'decimal(20,8)', 'decimal(20,8)', 'int']

    def values(self):
        """
        Return values in a list
        """
        return [self.Time] + \
               [self.Trade_id] + [self.Price] + [self.Amount] + [self.Type]

