
'''
============================================================
2.3 市场信息
以下函数均可通过exchange或exchanges[x]对象调用，例如：exchange.GetTicker(); 或 exchanges[0].GetTicker();返回市场行情
带有网络访问的API函数调用的重要提示：
# 在调用任何 访问交易所接口的 API 函数时（如 GetTicker、Buy、CancelOrder 等） 都有可能由于各种原因导致访问失败。
# 所以要对这些 函数的 调用做容错处理，举例: GetTicker 获取行情数据函数可能由于，交易所服务器问题，网络传输问题等
# 导致GetTicker 函数返回值 为 null ，这时就要对 GetTicker 的调用做容错处理。
# JS 描述

var ticker = exchange.GetTicker()
if(ticker == null){
    // 重试 ，或者其它处理逻辑。
}

# 另外，对于策略的容错性能测试，BotVS专门在回测中增加了独有的容错模式回测。
# 回测系统可以根据设置的参数随机给一些实盘时会发生网络访问的API调用返回一些失败调用时的返回值。
# 可以快速初步检测程序在实盘中的健壮性。
============================================================
'''
'''
exchange.GetTicker();
获取市场当前行情
返回值: Ticker结构体
Ticker结构体包含以下变量:
数据类型	变量名	说明
object	Info	交易所返回的原始结构
number	High	最高价
number	Low	最低价
number	Sell	卖一价
number	Buy	买一价
number	Last	最后成交价
number	Volume	最近成交量
function main(){
    var ticker = exchange.GetTicker();
    Log("High:", ticker.High, "Low:", ticker.Low, "Sell:", ticker.Sell, "Buy:", ticker.Buy, "Last:",
        ticker.Last, "Volume:", ticker.Volume);
}
'''
def GetTicker(cls):
    return

'''
exchange.GetDepth()

获取交易所订单薄

返回值:Depth结构体
Depth结构体包含两个结构体数组，分别是Asks[]和Bids[]，Asks和Bids包含以下结构体变量:

数据类型	变量名	说明
number	Price	价格
number	Amount	数量
例如我想获取当前卖二价，可以这么写代码:

function main(){
    var depth = exchange.GetDepth();
    var price = depth.Asks[1].Price;
    Log("卖二价为:", price);
}
'''
def GetDepth(cls):
    return

'''
（部分交易所不支持，具体返回的数据是多少范围内的成交记录，因交易所而定，需要根据具体情况处理）

exchange.GetTrades()

获取交易所交易历史（非自己）

返回值: Trade 结构体 数组
Trade 结构体

数据类型	变量名	说明
string 或 number （根据交易所返回类型而定）	Id	交易所返回的此Trade的唯一Id
number	Time	时间Unix timestamp 毫秒
number	Price	价格
number	Amount	数量
const	Type	订单类型:ORDER_TYPE_BUY, ORDER_TYPE_SELL。分别为买单，值为0，卖单，值为1
//在模拟回测中数据为空，必须实盘才有交易历史
function main(){
    var trades = exchange.GetTrades();
    Log("id:", trades[0].Id, "time:", trades[0].Time, "Price:", trades[0].Price, "Amount:", trades[0].Amount,
        "type:", trades[0].Type);
'''
def GetTrades(cls):
    return

'''
（部分交易所没有提供K线接口，托管者实时收集数据生成K线）

exchange.GetRecords(Period)

返回一个K线历史, K线周期在创建机器人时指定 ，如果 在调用 exchange.GetRecords() 函数时 指定了参数，
获取的就是按照该参数周期的K线数据，如果没有参数，
按照机器人参数上设置的K线周期或者回测页面设置的K线周期返回K线数据。
参数值:PERIOD_M1 指1分钟, PERIOD_M5 指5分钟, PERIOD_M15 指15分钟, PERIOD_M30 指30分钟, PERIOD_H1 指1小时, PERIOD_D1 指一天。

返回值: Record结构体数组
K线数据， 会随时间累积，最多累积到2000根，然后会更新加入一根，同时删除一根最早时间的K线柱（如队列进出）。
Record结构体包含以下变量:

数据类型	变量名	说明
number	Time	一个时间戳, 精确到毫秒，与Javascript的 new Date().getTime() 得到的结果格式一样
number	Open	开盘价
number	High	最高价
number	Low	最低价
number	Close	收盘价
number	Volume	交易量
function main(){
    var records = exchange.GetRecords(PERIOD_H1);
    Log("第一根k线数据为，Time:", records[0].Time, "Open:", records[0].Open, "High:", records[0].High,
        "Low:", records[0].Close, "Volume:", records[0].Volume);
    Log("第二根k线数据为，Time:", records[1].Time, "Open:", records[1].Open, "High:", records[1].High,
        "Low:", records[1].Close, "Volume:", records[1].Volume);
}
注意：

GetRecords 接口 获取K线数据 有2种情况：

1 交易所提供了K线数据接口，这种情况，获取的数据是交易所直接返回的数据。

2 交易所没有提供K线数据接口，BotVS 底层在 每次用户调用GetRecords 时 获取 交易所最近成交记录（即 GetTrades() 函数，合成K线数据。）

详细 参见帖子： 交易所 API 特殊问题汇总
https://www.botvs.com/bbs-topic/812
'''
def GetRecords(cls):
    return
'''
exchange.GetRawJSON()

返回最后一次REST API请求返回的原始内容(字符串), 可以用来自己解析扩展信息

返回值 : string类型
模拟测试的话，会一直返回一个空字符串, 只在真实环境下有效

function main(){
    exchange.GetAccount(); 
    var obj = JSON.parse(exchange.GetRawJSON());
    Log(obj);
}
'''
def GetRawJSON(cls):
    return

'''
exchange.GetRate()
返回交易所使用的流通货币与当前显示的计价货币的汇率, 返回1表示禁用汇率转换
返回值:number类型
# 注意： 如果没有调用 exchange.SetRate() 设置过 转换汇率 ， GetRate 默认返回的汇率值是 1 ，
# 即 当前显示的 计价货币 没有发生 过 汇率转换。
# 如果使用 exchange.SetRate() 设置过一个汇率值，例如 7， 那么 当前 exchange 这个交易所对象代表的交易所的流通货币
# 计价的 行情 、深度、下单价格 等等所有 价格信息，都会被 乘以 设置的汇率 7 ，进行转换。
# 例如 exchange 是 以美元为计价货币的交易所，  exchange.SetRate(7) 后， 机器人所有价格都会被 乘 7 转换成 接近
# CNY 的价格。 此时 使用 GetRate 获取的 汇率值  就是 7。
'''
def GetRate(cls):
    return
'''
exchange.GetUSDCNY()
返回美元最新汇率(yahoo提供的数据源)
返回值:number类型
'''
def GetUSDCNY(cls):
    return
'''
exchange.IO("websocket")
切换行情通信协议到websocket(默认为rest),切换之后获取行情的方式会改变,GetTicker()和GetDepth()将会切换为websocket协议来更新,由原来的主动获取行情数据变为被动获取行情数据
目前只支持火币和OK交易所
exchange.IO("mode", 0)
立即返回模式, 如果当前还没有接收到交易所最新的行情数据推送, 就立即返回旧的行情数据,如果有新的数据就返回新的数据
exchange.IO("mode", 1)
缓存模式(默认模式),如果当前还没有收到交易所最新的行情数据(同上一次接口获取的数据比较), 就等待接收然后再返回, 如果调用该函数之前收到了最新的行情数据,就立即返回最新的数据
exchange.IO("mode", 2)
强制更新模式, 进入等待一直到接收到交易所下一次的最新推送数据后返回
如果想第一时间获取最新的行情可以切换到websocket后不Sleep的立即检测数据, GetTicker, GetDepth用缓存模式进行工作,如：
exchange.IO("websocket");
while (true) {
  Log(exchange.GetTicker());
}
'''
def IO(cls):
    return

'''
============================================================
2.4 交易操作
以下函数均可通过exchange或exchanges[x]对象调用，例如：exchange.Sell(100, 1); 在交易所下一个价格为100，数量为1的买单
============================================================
'''
'''
exchange.Buy(Price, Amount)
下买单, 返回一个订单ID
参数值： price为订单价格，number类型，Amount为订单数量，number类型
返回值：string类型 或 数值类型 （具体类型根据各个交易所返回类型而定。）
返回订单编号，可用于查询订单信息和取消订单
function main(){
    var id = exchange.Buy(100, 1);
    Log("id:", id);
}
'''
def Buy(cls):
    return
'''
exchange.Sell(Price, Amount)
下卖单，返回一个订单ID
参数值：price为订单价格，number类型，Amount为订单数量，number类型
返回值：string类型 或 数值类型 （具体类型根据各个交易所返回类型而定。）
返回订单编号，可用于查询订单信息和取消订单
function main(){
    var id = exchange.Sell(100, 1);
    Log("id:", id);
}
'''
def Sell(cls):
    return
'''
exchange.CancelOrder(orderId)
取消某个订单
参数值：orderid为订单编号，string类型 或 数值类型。 （具体类型根据各个交易所下单时返回类型而定）
返回值：bool类型
返回操作结果，true表示取消订单请求发送成功，false取消订单请求发送失败（只是发送请求成功，交易所是否取消订单最好调用exchange.GetOrders()查看）
function main(){
    var id = exchange.Sell(99999, 1);
    exchange.CancelOrder(id);
}
'''
def CancelOrder(cls):
    return
'''
（部分交易所不支持）
exchange.GetOrder(orderId)
根据订单号获取订单详情
参数值: orderid为要获取的订单号，string类型 或 数值类型。（具体类型根据各个交易所返回类型而定）
返回值: Order结构体
数据类型	变量名	说明
object	Info	交易所返回的原始结构
string	Id	交易单唯一标识
number	Price	下单价格
number	Amount	下单数量
number	DealAmount	成交数量
number	AvgPrice	成交均价（有些交易所 不支持该 字段，不支持则设置0）
const	Status	订单状态, ORDER_STATE_PENDING : 未完成ORDER_STATE_CLOSED :已完成ORDER_STATE_CANCELED : 已取消
const	Type	订单类型, ORDER_TYPE_BUY :买单，ORDER_TYPE_SELL : 卖单
function main(){
    var id = exchange.Sell(99999, 1);
    var order = exchange.GetOrder(id);//参数id为订单号码，需填入你想要查询的订单的号码
    Log("Id", order.Id, "Price:", order.Price, "Amount:", order.Amount, "DealAmount:",
        order.DealAmount, "Status:", order.Status, "Type:", order.Type);
}
'''
def GetOrder(cls):
    return
'''
exchange.GetOrders()
获取所有未完成的订单
返回值: Order结构体数组
order结构体可参考GetOrder()函数说明
function main(){
    exchange.Sell(99999, 1);
    exchange.Sell(88888, 1);
    var orders = exchange.GetOrders();
    Log("未完成订单一的信息,ID:", orders[0].Id, "Price:", orders[0].Price, "Amount:", orders[0].Amount,
        "DealAmount:", orders[0].DeadAmount, "type:", orders[0].Type);
    Log("未完成订单二的信息,ID:", orders[1].Id, "Price:", orders[1].Price, "Amount:", orders[1].Amount,
        "DealAmount:", orders[1].DeadAmount, "type:", orders[1].Type);
}
GetOrders() 函数 获取的是当前设置的 交易对 或者 OKEX合约 的未完成挂单信息。
// 测试 OKex 合约 交易， GetOrders 获取的是否是 所有 未完成合约订单。
function main(){
    var ticker = exchange.GetTicker()
    Log(ticker)
    // 下一个 当周的  买单 ，价格减去 50 保证 不会成交，挂单。
    exchange.SetContractType("this_week")
    exchange.SetDirection("buy")
    exchange.Buy(ticker.Last - 50, 1)
    // 下一个 季度的  卖单， 价格加上 50 保证 不会成交，挂单，并已经切换成了 季度合约。
    exchange.SetContractType("quarter")
    exchange.SetDirection("sell")
    exchange.Sell(ticker.Last + 50, 1)
    // 获取 未完成的订单
    Log("orders", exchange.GetOrders())
}
获取的未完成的订单信息：[{"Id":17116430886,"Amount":1,"Price":808.4,"DealAmount":0,"AvgPrice":0,"Status":0,"Type":1,"ContractType":"quarter"}]
由此可见，GetOrders 获取的订单 仅仅是当前 设置合约的未完成的订单。
'''
def GetOrders(cls):
    return
'''
exchange.SetPrecision(PricePrecision, AmountPrecision)
设置价格与品种下单量的小数位精度, 设置后会自动截断
参数值：PricePrecision为number类型，用来控制价格后面的小数点位，AmountPrecision为number类型，用来控制数量后面的小数点位
PricePrecision和AmountPrecision都必须是整型number
function main(){
    exchange.SetPrecision(2, 3); //设置价格小数位精度为2位, 品种下单量小数位精度为3位
}    
# 注意：回测不支持该函数。
'''
def SetPrecision(cls):
    return
'''
exchange.SetRate(scale)
设置交易所的流通货币的汇率
参数值：scale为number类型
返回值：为number类型
function main(){
    exchange.SetRate();  // 如果不加参数，则恢复系统内置汇率 
    exchange.SetRate(1); // 就是禁用汇率转换
}
# 注意： 如果没有调用 exchange.SetRate() 设置过 转换汇率 ， GetRate 默认返回的汇率值是 1 ，
# 即 当前显示的 计价货币 没有发生 过 汇率转换。
# 如果使用 exchange.SetRate() 设置过一个汇率值，例如 7， 那么 当前 exchange 这个交易所对象代表的交易所的流通货币
# 计价的 行情 、深度、下单价格 等等所有 价格信息，都会被 乘以 设置的汇率 7 ，进行转换。
# 例如 exchange 是 以美元为计价货币的交易所，  exchange.SetRate(7) 后， 机器人所有价格都会被 乘 7 转换成 接近
# CNY 的价格。 此时 使用 GetRate 获取的 汇率值  就是 7。
'''
def SetRate(cls):
    return
'''
exchange.IO("api", httpMethod, resource, params)
调用交易所其它功能接口
参数值：httpMehod为string类型，填入请求类型"POST"或者"GET",resource为string类型,填入路径,params为string类型，填入交互参数
使用此函数需要去交易所了解该交易所的API接口，用来扩展BotVS没有添加的功能(提交POST请求不必担心参数加密过程，BotVS在底层已经完成加密，只要填入相应参数即可)。
举个例子，比如BotVS平台目前不支持bitfinex交易所的保证金杠杆交易，我们可以通过IO函数来实现这一个功能,按照以下步骤。
先找到bitfinex的API接口说明页面：bitfinex。
然后我们得知下单是以POST请求交互的，所以我们把参数httpMethod传入"POST"保证金交易的下单地址为：'https://api.bitfinex.com/v1/order/new'。因为BotVS已经在内部指定了根地址，所以我们只需要把参数resource的值传入"/v1/order/new"就行了。
然后还剩params参数没有填入，params变量代表了所要交互的信息，我们把各种信息以"&"符号链接起来发送即可，我们先到bitfinex查看得知下一个买单或卖单需要5个参数，分别是：symbol，amount，price，side，type。我们分别给这5个参数赋值，假如我们要买莱特币LTC，数量为1个，价格为10，为保证金交易模式，那么我们可以构造这么一个字符串："symbol=ltc&amount=1&price=10&side=buy&type=limit"。
最后我们把以上结合通过一行代码即可交易：
function main(){
    exchange.IO("api","POST","/v1/order/new","symbol=ltc&amount=1&price=10&side=buy&type=limit");
}
全部代码例子可到Botvs策略广场：bitfinex保证金交易查看。
OKEX 范例：
function main(){
    //            URL: /api/v1/future_position.do
    /*
    symbol        String 是  btc_usd   ltc_usd    eth_usd    etc_usd    bch_usd
    contract_type String 是  合约类型: this_week:当周   next_week:下周   quarter:季度
    api_key       String 是  用户申请的apiKey
    sign          String 是  请求参数的签名    
    */
    var ret = exchange.IO("api", "POST", "/api/v1/future_position.do", "symbol=eth_usd&contract_type=this_week")

    Log(ret)
}
返回数据：
{
    "result": true,
    "holding": [{
        "buy_available": 0,
        "contract_id": 201876560020041,
        "sell_amount": 0,
        "sell_profit_real": 0.07166192,
        "buy_profit_real": -0.00003518,
        "contract_type": "this_week",
        "create_date": 1516881053000,
        "buy_price_avg": 1093.737,
        "lever_rate": 10,
        "sell_price_cost": 933.14087684,
        "buy_price_cost": 1093.737,
        "sell_price_avg": 933.14087684,
        "sell_available": 0,
        "symbol": "eth_usd",
        "buy_amount": 0
    }],
    "force_liqu_price": "0.000"
}
IO 函数修改机器人的其它设置
切换当前交易所的交易对
exchange.IO("currency", "ETH_BTC")
这样就会通过代码切换 机器人 创建时配置的 交易对。
# 注意：
1、如果 在OKEX 或者 火币 PRO  切换了 websocket 协议 模式，则不能 使用exchange.IO("currency", "XXX_YYY")
切换币种。
2、exchange.IO("currency", "ETH_BTC")   # 仅支持 实盘，回测不支持。
'''
def  IO(cls):
    return
'''
exchange.Go(Method, Args…)
多线程异步支持函数, 可以把所有支持的函数的操作变成异步并发的.(只支持数字货币交易平台)
参数值：Method为string类型，函数名
# 注意：该函数 只在实盘运行时 创建多线程执行任务，回测不支持多线程并发执行任务（回测可用，但是还是顺序执行）。
支持的函数: GetTicker, GetDepth, GetTrades, GetRecords, GetAccount, GetOrders, GetOrder, CancelOrder, Buy, Sell, GetPosition
function main(){
    var a = exchange.Go("GetTicker"); //GetTicker 异步多线程执行 
    var b = exchange.Go("GetDepth"); 
    var c = exchange.Go("Buy", 1000, 0.1); 
    var d = exchange.Go("GetRecords", PERIOD_H1);
    //上面四种操作是并发多线程异步执行, 不会耗时, 立即返回的
    var ticker = a.wait(); //调用wait方法等待返回异步获取ticker结果 
    var depth = b.wait(); //返回深度, 如果获取失败也是有可能返回null的 
    var orderId = c.wait(1000); //返回订单号, 限定1秒超时, 超时返回undefined, 此对像可以继续调用wait等待如果上次wait超时 
}
注意: 判断undefiend要用typeof(xx) === “undefined”, 因为null==undefined在JavaScript里是成立的
var records = d.wait(); //等待K线结果 
var ret = d.wait();  //这里wait了一个已经wait过且结束的异步操作, 会返回null, 并记录出错信息. 
Python与Javascript的区别, Python的wait返回两个参数, 第一个是异步的api返回的结果, 第二个表示是异步调用是否完成
ret, ok = d.wait(); //ok是一定返回True的, 除非策略被停止 
ret, ok = d.wait(100); //ok返回False, 如果等待超时, 或者wait了一个已经结束的实例
'''
def Go(cls):
    return
'''
============================================================
2.5 账户信息
============================================================
'''
'''
exchange.GetAccount()
将返回交易所账户信息
返回值: Account结构结构体
Account结构体包含以下变量:
数据类型	变量名	说明
object	Info	交易所返回的原始结构
number	Balance	余额(订价货币余额, ETH_BTC的话BTC为订价货币)
number	FrozenBalance	冻结的余额
number	Stocks	交易货币的可用数量, 数字货币现货为当前可操作币的余额(去掉冻结的币), 数字货币期货的话为合约当前可用保证金(传统期货无此属性) 。
number	FrozenStocks	冻结的交易货币的可用数量(传统期货无此属性)
function main(){
    var account = exchange.GetAccount();
    Log("账户信息，Balance:", account.Balance, "FrozenBalance:", account.FrozenBalance, "Stocks:",
        account.Stocks, "FrozenStocks:", account.FrozenStocks);
}
'''
def GetAccount(cls):
    return
'''
exchange.GetName()
返回交易所名称
返回值: string类型
'''
def GetName(cls):
    return
'''
exchange.GetLabel()
返回交易所自定义的标签
返回值:string类型
'''
def GetLabel(cls):
    return
'''
exchange.GetCurrency()
返回交易所操作的货币对名称如LTC_BTC, 传统期货CTP返回的固定为STOCK.
返回值:string类型
'''
def GetCurrency(cls):
    return
'''
exchange.GetQuoteCurrency()
返回交易所操作的基础货币名称, 例如BTC_CNY就返回CNY, ETH_BTC就返回BTC
返回值:string类型
'''
def GetQuoteCurrency(cls):
    return

'''
==============================================================
2.6 期货交易
期货支持传统商品期货CTP协议, BTC期货:OKCoin，BitMEX
=============================================================
'''
'''
exchange.GetPosition()
获取当前持仓信息, OKCoin可以传入一个参数, 指定要获取的合约类型
返回值：position结构体数组
position结构体包含以下变量：
数据类型	变量名	说明
object	Info	交易所返回的原始结构
number	MarginLevel	杆杠大小, OKCoin为10或者20,OK期货的全仓模式返回为固定的10, 因为原生API不支持
number	Amount	持仓量,OKCoin表示合约的份数(整数且大于1)
number	CanCover	可平量, 只有股票有此选项, 表示可以平仓的数量(股票为T+1)今日仓不能平
number	FrozenAmount	仓位冻结量
number	Price	持仓均价
number	Profit	商品期货：持仓盯市盈亏，数字货币：(数字货币单位：BTC/LTC, 传统期货单位:RMB, 股票不支持此字段, 注: OKCoin期货全仓情况下指实现盈余, 并非持仓盈亏, 逐仓下指持仓盈亏)
const	Type	PD_LONG为多头仓位(CTP中用closebuy_today平仓), PD_SHORT为空头仓位(CTP用closesell_today)平仓, (CTP期货中)PD_LONG_YD为昨日多头仓位(用closebuy平), PD_SHORT_YD为昨日空头仓位(用closesell平)
string	ContractType	商品期货为合约代码, 股票为’交易所代码_股票代码’, 具体参数SetContractType的传入类型
# 注意： GetPosition 函数获取的是 所有 持仓品种的 持仓信息。
function main(){
    exchange.SetContractType("this_week");
    exchange.SetMarginLevel(10);
    exchange.SetDirection("buy");
    exchange.Buy(10000, 2);
    position = exchange.GetPosition();
    Log("Amount:", position[0].Amount, "FrozenAmount:", position[0].FrozenAmount, "Price:",
        position[0].Price, "Profit:", position[0].Profit, "Type:", position[0].Type,
        "ContractType:", position[0].ContractType);
}
'''
def GetPosition(cls):
    return
'''
exchange.SetMarginLevel(MarginLevel)
设置杆杠大小
参数值：number整型
设置Buy(多单)或者Sell(空单)的杆杠大小, MarginLevel有5, 10, 20 三个可选参数,OKCoin支持10倍和20倍，如:
exchange.SetMarginLevel(10)
'''
def SetMarginLevel(cls):
    return
'''
exchange.SetDirection(Direction)
设置Buy或者Sell下单类型
参数值：string类型
Direction可以取buy, closebuy, sell, closesell四个参数, 传统期货多出closebuy_today,与closesell_today, 指平今仓, 默认为closebuy/closesell为平昨仓。对于CTP传统期货, 可以设置第二个参数”1”或者”2”或者”3”, 分别指”投机”, “套利”, “套保”, 不设置默认为投机，股票只支持buy与closebuy, 因为股票只能买跟平仓
function main(){
    exchange.SetMarginLevel(5); //设置杠杆为5倍 
    exchange.SetDirection("buy"); //设置下单类型为做多 
    exchange.Buy(1000, 2); //以1000的价格，合约数量为2下单 
    exchange.SetMarginLevel(5); 
    exchange.SetDirection("closebuy"); 
    exchange.Sell(1000, 2);
}
'''
def SetDirection(cls):
    return
'''
SetContractType(ContractType)
设置合约类型
参数值：string类型
传统的CTP期货的ContractType就是指的合约ID, 如SetContractType("au1506") 返回合约的详细信息, 如最少一次买多少, 手续费, 交割时间等，主力连续合约为代码为888如MA888, 连续指数合约为000如MA000, 888与000为虚拟合约交易只支持回测, 实盘只支持获取行情。
订阅虚拟合约成功以后, 返回的字段里面的InstrumentID是主力合约(会在订阅同时获取), 方便策略实盘下单做映射用。
股票合约格式为 股票代码.(SH/SZ), SH指上交所, SZ指深交所, 如000001.SZ就是指深交所的平安银行。
OKCoin期货有this_week, next_week, quarter三个参数
exchange.SetContractType("this_week"); //设置为当周合约
'''
def SetContractType(cls):
    return
'''
传统商品期货扩展的IO功能
exchange.IO("status");
返回true证明与CTP服务器行情与数据的两台服务器都连接正常
while (!exchange.IO("status")) {
    Sleep(3000);
    LogStatus("正在等待与交易服务器连接, " + new Date());
}
exchange.IO("wait");
当前交易所有任何品种更新行情信息时才返回, 可带第二个参数(毫秒数)指定超时, 超时返回null, 正常返回EventTick结构。 exchange.IO("wait") 结合 exchange.IO("mode", 0) 函数使用（说明 exchange.IO("mode", 0) ：立即返回模式, 如果当前还没有接收到交易所最新的行情数据推送, 就立即返回旧的行情数据,如果有新的数据就返回新的数据 ）。这样配合使用就可以使程序在有最新行情时进行响应，执行程序逻辑。
// 代码节选自 “商品期货交易类库 ”
$.CTA = function(contractType, onTick, interval) {
    SetErrorFilter("login|ready|初始化")
    if (typeof(interval) !== 'number') {
        interval = 500
    }
    exchange.IO("mode", 0)               // 切换 为立即返回模式，不会导致程序卡在获取行情的函数调用位置。
                                         // 也不会因为一个品种 行情没有更新而导致程序等待。
    ...
}
// 队列 任务处理 代码块
self.poll = function() {
    var processed = 0
    if (self.tasks.length > 0) {
        _.each(self.tasks, function(task) {
            if (!task.finished) {
                processed++
                self.pollTask(task)
            }
        })
        if (processed == 0) {
            self.tasks = []
        }
    } else {
        // wait for master market update
        exchange.IO("wait")                // 此处使用 exchange.IO("wait") 等待任意品种更新行情。 
    }
    return processed
}
exchange.IO("wait_any");
同上, 但是指的是有任何一个交易所收到行情信息时就返回,EventTick里的Index指交易所索引
// 用于 多交易所对象（多个期货公司前置服务器） 收集行情数据时。 
exchange.IO("wait_order");
等待任意订单的交易信息, 返回一个Json结构{Index: 交易所索引, Nano: 事件纳秒级时间, Order: 订单信息} 超时返回json的null对像
exchange.IO("instruments");
返回交易所所有的合约列表{合约名: 详情}字典形式, 只支持实盘
Log("开始获取所有合约");
var instruments = _C(exchange.IO, "instruments");
Log("合约列表获取成功");
var len = 0;
for (var instrumentId in instruments) {
    len++;
}
Log("合约列表长度为:", len);
exchange.IO("products");
返回交易所所有的产品列表{产品名: 详情}字典形式, 只支持实盘
exchange.IO("subscribed");
返回已订阅行情的合约, 格式同上, 只支持实盘
exchange.IO("settlement");
结算单查询, 不加第二个参数默认返回之前一个交易日的, 加参数如”20170317”指返回20170317的结算单, 只支持实盘
'''
def IO(cls):
    return

'''
2.6.6 传统商品期货

传统商品期货API获取更多信息
exchange.GetAccount();
Log(exchange.GetRawJSON());//在GetAccount成功后调用, 获取更详细的账户信息, 可以用JSON.parse解析。 
也支持GetTicker, GetDepth后的exchange.GetRawJSON(), 以及GetPosition与GetOrders,GetOrder这三个调用后的详细反馈数据。

期货交易中Buy, Sell, CancelOrder和现货交易的区别
Buy或Sell之前需要调用SetMarginLevel和SetDirection明确操作类型，如:

exchange.SetDirection("sell");  
exchange.Sell(1000, 2);
exchange.SetDirection("buy"); 
exchange.CancelOrder(123);
商品期货支持自定义订单类型 （支持实盘，回测暂不支持）
以后缀方式指定, 附加在_后面比如

exchange.SetDirection("buy_ioc");
exchange.SetDirection("sell_gtd-20170111"); // 交易所暂不支持这种类型
后缀	意义	对应CTP原始值
ioc	立即完成，否则撤销	THOST_FTDC_TC_IOC
gfs	本节有效	THOST_FTDC_TC_GFS
gfd	当日有效	THOST_FTDC_TC_GFD
gtd	指定日期前有效	THOST_FTDC_TC_GTD
gtc	撤销前有效	THOST_FTDC_TC_GTC
gfa	集合竞价有效	THOST_FTDC_TC_GFA
'''