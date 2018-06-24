'''
账户信息, 由GetAccount函数返回
{
    Balance	        :余额(人民币或者美元, 在Poloniex交易所里ETC_BTC这样的品种, Balance就指的是BTC的数量, Stocks指的是ETC数量)
    FrozenBalance	:冻结的余额
    Stocks	        :BTC/LTC数量, 数字货币现货为当前可操作币的余额(去掉冻结的币), 数字货币期货的话为合约当前可用保证金(传统期货无此属性)
    FrozenStocks	:冻结的BTC/LTC数量(传统期货无此属性)
}
'''