'''
期货交易中的持有仓位信息, 由GetPosition()函数返回此结构数组
{
    MarginLevel     :杆杠大小, OKCoin为10或者20。
    Amount          :持仓量, OKCoin表示合约的份数(整数且大于1)
    CanCover        :可平量, 只有股票有此选项, 表示可以平仓的数量(股票为T+1)今日仓不能平
    FrozenAmount    :仓位冻结量
    Price           :持仓均价
    Profit          :持仓浮动盈亏(数据货币单位：BTC/LTC, 传统期货单位:RMB, 股票不支持此字段, 注: OKCoin期货全仓情况下指实现盈余, 并非持仓盈亏, 逐仓下指持仓盈亏)
    Type            :PD_LONG为多头仓位(CTP中用closebuy_today平仓), PD_SHORT为空头仓位(CTP用closesell_today)平仓, (CTP期货中)PD_LONG_YD为咋日多头仓位(用closebuy平), PD_SHORT_YD为咋日空头仓位(用closesell平)
    ContractType    :商品期货为合约代码, 股票为'交易所代码_股票代码', 具体参数SetContractType的传入类型
}
'''