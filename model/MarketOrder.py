'''
市场深度单，即 GetDepth 返回数据中 Bids 、Asks 数组中的元素的数据结构。
{
    Price	:价格
    Amount	:数量
}
'''
import copy


class MarketOrder:
    """
    Abstract class of a market data
    """
    class Side:
        ORDER_TYPE_BUY = 0
        ORDER_TYPE_SELL = 1
        NONE = 2

    class Status:
        ORDER_STATE_PENDING = 0           #未完成
        ORDER_STATE_CLOSED = 1            #已完成
        ORDER_STATE_CANCELED = 2          #已取消

    def __init__(self):
        """
        Constructor
        """
        pass

    def __init__(self, price=0.0, amount=0.0):
        """
        Constructor
        """
        self.Price = price
        self.Amount = amount

    def copy(self):
        return copy.deepcopy(self)

    @staticmethod
    def parse_side(value):
        """
        Decode the value to Side (BUY/SELL)
        :param value: Integer or string
        :return: Side (NONE, BUY, SELL)
        """
        if type(value) != int:
            value = value.lower()
            if value == 'buy' or value == 'bid' or value == 'b':
                return MarketOrder.Side.ORDER_TYPE_BUY
            elif value == 'sell' or value == 'ask' or value == 's':
                return MarketOrder.Side.ORDER_TYPE_SELL
            else:
                return MarketOrder.Side.NONE

        if value == 1:
            return MarketOrder.Side.ORDER_TYPE_BUY
        elif value == 2:
            return MarketOrder.Side.ORDER_TYPE_SELL
        else:
            raise Exception("Cannot parse the side (%s)" % value)



