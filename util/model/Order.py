'''
订单结构, 由GetOrder , GetOrders函数返回
{
    Id          :交易单唯一标识
    Price       :下单价格
    Amount      :下单数量
    DealAmount  :成交数量
    AvgPrice    :成交均价，                     # 注意 ，有些交易所不提供该数据，不提供的设置为 0 。
    Status      :订单状态, 参考常量里的订单状态
    Type        :订单类型, 参考常量里的订单类型
}
订单的状态 Order结构里的Status值

全局常量	意义
ORDER_STATE_PENDING	未完成
ORDER_STATE_CLOSED	已关闭
ORDER_STATE_CANCELED	已取消
订单的类型 Order结构里的Type值

全局常量	意义
ORDER_TYPE_BUY	买单
ORDER_TYPE_SELL	卖单
'''
from datetime import datetime


class Order:

    def __init__(self):
        """
        amount:委托数量
        create_date: 委托时间
        avg_price:平均成交价
        deal_amount:成交数量
        order_id:订单ID
        orders_id:订单ID(不建议使用)
        price:委托价格
        status:-1:已撤销  0:未成交  1:部分成交  2:完全成交 3:撤单处理中
        type:buy买入 / sell 卖出 / buy_market:市价买入 / sell_market:市价卖出
        """
        self.Exchange = ''
        self.Order_id = ''
        self.Orders_id = ''
        self.Create_date = datetime(2000, 1, 1, 0, 0, 0).strftime("%Y%m%d %H:%M:%S.%f")
        self.Symbol = ''
        self.Amount = 0.0
        self.Price = 0.0
        self.Avg_price = 0.0
        self.Deal_amount = 0.0
        self.Status = ''
        self.Type = ''

    @staticmethod
    def columns():
        """
        Return static columns names
        """
        return ['exchange', 'order_id', 'orders_id', 'create_date', 'symbol',
                'amount', 'price', 'avg_price', 'Deal_amount',
                'status', 'type']

    @staticmethod
    def types():
        """
        Return static column types
        """
        return ['varchar(25)', 'varchar(25)', 'varchar(25)', 'varchar(25)', 'varchar(15)',
                'decimal(20,8)', 'decimal(20,8)', 'decimal(20,8)', 'decimal(20,8)',
                'varchar(5)', 'varchar(15)']

    def print_detail(self):
        total_with = 12 + 9*15 + 20
        print('=' * total_with)
        format_tile = "%-10s%15s%15s%20s%15s" \
                      "%15s%15s%15s%15s" \
                      "%15s%15s"
        print(format_tile % ("exchange", "order_id", "orders_id", "create_date", "symbol",
                             "amount", "price", "avg_price", "Deal_amount",
                             "status", "type"))
        print('-' * total_with)
        format_value = "%-10s%15s%15s%20s%15s" \
                       "%15.8f%15.8f%15.4f%15.4f" \
                       "%15s%15s"
        print(format_value % (self.Exchange, self.Order_id, self.Orders_id, self.Create_date, self.Symbol,
                              self.Amount, self.Price, self.Avg_price, self.Deal_amount,
                              self.Status, self.Type))
        print('=' * total_with)
        print("        status: -1:已撤销  0:未成交  1:部分成交  2:完全成交 3:撤单处理中")
        print("          type: buy:买入  sell:卖出  buy_market:市价买入  sell_market:市价卖出")


class Orders:
    def __init__(self):
        self.Orders_list = []

    def add_order(self, order):
        self.Orders_list.append(order)

    def add_orders(self, orders):
        if len(orders.Orders_list) > 0:
            self.Orders_list.extend(orders.Orders_list)

    def sort_orders_by_symbol(self):
        self.Orders_list.sort(key=lambda x: x.Symbol, reverse=True)

    def print_detail(self):
        if len(self.Orders_list) == 0:
            return
        total_with = 12 + 9*15 + 20
        print('=' * total_with)
        format_tile = "%-10s%15s%15s%20s%15s" \
                      "%15s%15s%15s%15s" \
                      "%15s%15s"
        print(format_tile % ("exchange", "order_id", "orders_id", "create_date", "symbol",
                             "amount", "price", "avg_price", "Deal_amount",
                             "status", "type"))
        print('-' * total_with)
        format_value = "%-10s%15s%15s%20s%15s" \
                       "%15.8f%15.8f%15.4f%15.4f" \
                       "%15s%15s"
        for order in self.Orders_list:
            print(format_value % (order.Exchange, order.Order_id, order.Orders_id, order.Create_date, order.Symbol,
                                  order.Amount, order.Price, order.Avg_price, order.Deal_amount,
                                  order.Status, order.Type))
        print('=' * total_with)
        print("        status: -1:已撤销  0:未成交  1:部分成交  2:完全成交 3:撤单处理中")
        print("          type: buy:买入  sell:卖出  buy_market:市价买入  sell_market:市价卖出")
