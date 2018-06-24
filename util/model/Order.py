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