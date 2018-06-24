from datetime import datetime
from talang.util.model import MarketOrder
'''
市场深度,由GetDepth函数返回
{
    Asks	:卖单数组, MarketOrder数组, 按价格从低向高排序
    Bids	:买单数组, MarketOrder数组, 按价格从高向低排序
}
'''


class Depth(MarketOrder):
    """
    L2 price depth. Container of date, time, bid and ask up to 5 levels
    """
    def __init__(self, depth=5):
        """
        Constructor
        :param depth: Number of depth
        """
        MarketOrder.__init__(self)
        self.date_time = datetime(2000, 1, 1, 0, 0, 0).strftime("%Y%m%d %H:%M:%S.%f")
        self.depth = depth
        self.bids = [MarketOrder() for i in range(0, self.depth)]
        self.asks = [MarketOrder() for i in range(0, self.depth)]

    @staticmethod
    def columns():
        """
        Return static columns names
        """
        return ['date_time',
                'b1', 'b2', 'b3', 'b4', 'b5',
                'a1', 'a2', 'a3', 'a4', 'a5',
                'bq1', 'bq2', 'bq3', 'bq4', 'bq5',
                'aq1', 'aq2', 'aq3', 'aq4', 'aq5']

    @staticmethod
    def types():
        """
        Return static column types
        """
        return ['varchar(25)'] + \
               ['decimal(10,5)'] * 10 + \
               ['decimal(20,8)'] * 10

    def values(self):
        """
        Return values in a list
        """
        if self.depth == 5:
            return [self.date_time] + \
                   [b.price for b in self.bids] + \
                   [a.price for a in self.asks] + \
                   [b.volume for b in self.bids] + \
                   [a.volume for a in self.asks]
        else:
            return [self.date_time] + \
                   [b.price for b in self.bids[0:5]] + \
                   [a.price for a in self.asks[0:5]] + \
                   [b.volume for b in self.bids[0:5]] + \
                   [a.volume for a in self.asks[0:5]]

    def sort_bids(self):
        """
        Sorting bids
        :return:
        """
        self.bids.sort(key=lambda x:x.price, reverse=True)
        if len(self.bids) > self.depth:
            self.bids = self.bids[0:self.depth]

    def sort_asks(self):
        """
        Sorting bids
        :return:
        """
        self.asks.sort(key=lambda x:x.price)
        if len(self.asks) > self.depth:
            self.asks = self.asks[0:self.depth]

    def copy(self):
        """
        Copy
        """
        ret = Depth(depth=self.depth)
        ret.date_time = self.date_time
        ret.bids = [e.copy() for e in self.bids]
        ret.asks = [e.copy() for e in self.asks]
        return ret

    def is_diff(self, depth):
        """
        Compare the first 5 price depth
        :param depth: Another Depth object
        :return: True if they are different
        """
        for i in range(0, 5):
            if abs(self.bids[i].Price - depth.bids[i].Price) > 1e-09 or \
               abs(self.bids[i].Amount - depth.bids[i].Amount) > 1e-09:
                return True
            elif abs(self.asks[i].Price - depth.asks[i].Price) > 1e-09 or \
                    abs(self.asks[i].Amount - depth.asks[i].Amount) > 1e-09:
                return True
        return False
