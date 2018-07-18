from datetime import datetime
from talang.util.model.ModelBase import ModelBase
import talang.util.util_data as ut

'''
获取所有交易历史(非自己),由GetTrades函数返回。
{
    Time	:时间(Unix timestamp 毫秒)
    Price	:价格
    Amount	:数量
    Type	:订单类型, 参考常量里的订单类型
}
'''


class Trade(ModelBase):
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
        self.result = ''  # result:True
        self.trade_id = ''
        self.price = 0.0
        self.amount = 0.0
        self.type = ''      #买卖类型：限价单(buy/sell) 市价单(buy_market/sell_market)


    @staticmethod
    def columns():
        """
        Return static columns names
        """
        return ['exchange', 'time', 'result', 'trade_id', 'price', 'amount', 'type']

    @staticmethod
    def types():
        """
        Return static column types
        """
        return ['varchar(25)', 'text', 'varchar(25)', 'varchar(25)', 'decimal(20,8)', 'decimal(20,8)', 'varchar(25)']

    def values(self):
        """
        Return values in a list
        """
        return [self.exchange] + [self.time] + [self.result] + \
               [self.trade_id] + [self.price] + [self.amount] + [self.type]



