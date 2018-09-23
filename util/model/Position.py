
from talang.util.model.ModelBase import ModelBase
import talang.util.util_data as ut
from talang.util.database.sqlite_client import SqliteClient

class Position(ModelBase):
    '''
    # Request
    POST https://www.okex.com/api/v1/future_position_4fix.do
    # Response
    {'result': True, 'holding': [
        {'buy_price_avg': 0, 'symbol': 'eth_usd', 'lever_rate': 10, 'buy_available': 0, 'contract_id': 201809210020060,
         'sell_risk_rate': '104.79', 'buy_amount': 0, 'buy_risk_rate': '1,000,000.00', 'profit_real': 0.00786862,
         'contract_type': 'next_week', 'sell_flatprice': '186.566', 'buy_bond': 0, 'sell_profit_lossratio': '4.79',
         'buy_flatprice': '0.000', 'buy_profit_lossratio': '0.00', 'sell_amount': 16, 'sell_bond': 0.09424238,
         'sell_price_cost': 169.775, 'buy_price_cost': 0, 'create_date': 1536571738000, 'sell_price_avg': 169.775,
         'sell_available': 16}]}
    '''
    def __init__(self):
        self.symbol = ''             #btc_usd ltc_usd eth_usd etc_usd bch_usd
        self.contract_id = ''        #合约id
        self.lever_rate = '10'       #杠杆倍数
        self.contract_type = 'next_week' #合约类型
        self.create_date = ''        #创建日期
        self.profit_real = 0         #已实现盈余

        self.buy_profit_lossratio=0  #多仓盈亏比
        self.buy_amount = 0          #多仓数量
        self.buy_available = 0       #多仓可平仓数量
        self.buy_bond = 0            #多仓保证金
        self.buy_price_avg = 0.0     #多仓开仓平均价
        self.buy_flatprice = 0       #多仓强平价格
        self.buy_price_cost = 0      #多仓结算基准价
        self.buy_risk_rate = '1000000' #

        self.sell_profit_lossratio=0 #空仓盈亏比
        self.sell_amount = 0         #空仓数量
        self.sell_available= 0       #空仓可平仓数量
        self.sell_bond = 0           #空仓保证金
        self.sell_price_avg = 0      #空仓开仓平均价
        self.sell_flatprice = 0      #空仓强平价格
        self.sell_price_cost = 0     #空仓结算基准价
        self.sell_risk_rate = '104.79' #

    def LongOrShort(self):
        result = ut.OKEX_NA
        if self.buy_amount > 0:
            result = ut.OKEX_LONG
        elif self.sell_amount > 0:
            result = ut.OKEX_SHORT
        return result

    def get_amount(self):
        result = 0
        if self.buy_amount > 0:
            result = self.buy_amount
        elif self.sell_amount > 0:
            result = self.sell_amount
        return result

    #强平的交易类型
    def get_liquidate_trade_type(self):
        '''
        1: 开多
        2: 开空
        3: 平多
        4: 平空
        :return:
        '''
        result = ut.OKEX_NA
        if self.buy_amount > 0:
            result = '3'
        elif self.sell_amount > 0:
            result = '4'
        return result

    @staticmethod
    def tablename():
        return 'position'

    @staticmethod
    def primary_key_index():
        return []

    @staticmethod
    def columns():
        """
        Return static columns names
        """
        return ['exchange', 'time', 'symbol', 'contract_id', 'lever_rate',
                'contract_type', 'create_date', 'profit_real',
                'buy_profit_lossratio', 'buy_amount', 'buy_available', 'buy_bond',
                'buy_price_avg', 'buy_flatprice', 'buy_price_cost', 'buy_risk_rate',
                'sell_profit_lossratio', 'sell_amount', 'sell_available', 'sell_bond',
                'sell_price_avg', 'sell_flatprice', 'sell_price_cost', 'sell_risk_rate']

    @staticmethod
    def types():
        return ['varchar(20)', 'varchar(25)', 'varchar(20)', 'text', 'varchar(10)',
                'varchar(20)', 'varchar(25)', 'decimal(10,5)',
                'decimal(15,6)', 'decimal(15,6)', 'decimal(15,6)', 'decimal(15,6)',
                'decimal(15,6)', 'decimal(15,6)', 'decimal(15,6)', 'varchar(25)',
                'decimal(15,6)', 'decimal(15,6)', 'decimal(15,6)', 'decimal(15,6)',
                'decimal(15,6)', 'decimal(15,6)', 'decimal(15,6)', 'varchar(25)']

    def values(self):
        return [self.exchange] + [self.time] + [self.symbol] + [self.contract_id] + [self.lever_rate] + \
                [self.contract_type] + [self.create_date] + [self.profit_real] + \
                [self.buy_profit_lossratio] + [self.buy_amount] + [self.buy_available] + [self.buy_bond] + \
                [self.buy_price_avg] + [self.buy_flatprice] + [self.buy_price_cost] + [self.buy_risk_rate] + \
                [self.sell_profit_lossratio] + [self.sell_amount] + [self.sell_available] + [self.sell_bond] + \
                [self.sell_price_avg] + [self.sell_flatprice] + [self.sell_price_cost] + [self.sell_risk_rate]


    def print_detail(self, i=1):

        total_with = 10 + 15 * 15

        if i == 1:
            print('=' * total_with)
            format_tile = "%-10s%-15s%15s%15s%10s%10s" \
                          "%15s%15s%15s" \
                          "%10s%10s%10s" \
                          "%10s%10s%10s"
            print(format_tile % ("No.", "contract_id", "time", "多空方向", "symbol", "杠杆倍数",
                                 "contract_type", "create_date", "已实现盈余",
                                 "多仓盈亏比","多仓数量", "多仓开仓平均价",
                                 "空仓盈亏比", "空仓数量", "空仓开仓平均价"
                                 ))
            print('-' * total_with)

        format_value = "%-10d%-20s%-15s%10s%10s%15s" \
                       "%12s%20s%15.4f" \
                       "%15.4f%15.4f%15.4f" \
                       "%15.4f%15.4f%15.4f"
        print(format_value % (
        i, self.contract_id, self.time, self.LongOrShort(), self.symbol, self.lever_rate,
        self.contract_type, self.create_date, self.profit_real,
        self.buy_profit_lossratio, self.buy_amount, self.buy_price_avg,
        self.sell_profit_lossratio, self.sell_amount, self.sell_price_avg
        ))


class Positions:
    def __init__(self):
        self.Positions_list = []

    def add_position(self, position):
        self.Positions_list.append(position)

    def add_positions(self, positions):
        if len(positions.Positions_list) > 0:
            self.Positions_list.extend(positions.Positions_list)

    def get_position(self, contract_id):
        for position in self.Positions_list:
            if position.contract_id == contract_id:
                return position
        return None

    def print_detail(self):
        if len(self.Positions_list) == 0:
            return
        i = 1
        for position in self.Positions_list:
            position.print_detail(i)
            i = i + 1


class PositionDatabase:
    def __init__(self):
        self.db_client = SqliteClient()
        self.db_client.connect(path=ut.SQLPLITE_PATH)
        self.is_database_defined = True
        return None

    #插入并替换，根据主键替换
    def insert_position_to_database(self, position):
        self.db_client.insert(position.tablename(), position.columns(), position.types(), position.values(),
                              position.primary_key_index(), False)






