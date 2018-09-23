from talang.util.model.ModelBase import ModelBase
import talang.util.util_data as ut
from datetime import datetime
from talang.util.database.sqlite_client import SqliteClient
import sqlite3


class GreedMark(ModelBase):
    def __init__(self):
        self.contract_id = ''                   # 合约id，订单号
        self.long_or_short = ut.OKEX_NA         #多空标志，默认'NA',

        self.loss_scope = -20                   # 强平止损幅度，-20表示亏损20%时候强平止损
        self.profit_scope = 20                  # 最低盈利幅度，超过此盈利幅度才考虑止盈强平,20表示20%
        self.profit_liquidation_scope = 20      # 盈利情况下，强平回调比例，20表示比盈利最高点回调20%的时候强平止盈

        self.amount = 0                         #合约单数，position的buy_amount 或 sell_amount的值
        self.last_profit_loss_ratio = 0         # 最近的上一次查询的盈亏比率
        self.now_profit_loss_ratio = 0          # 现在查询的“盈亏比率”
        self.top_profit_loss_ratio = 0          # 表示“盈亏比率”曾经达到的最高点
        self.bottom_profit_loss_ratio = 0       # 表示“盈亏比率”曾经达到的最低点

        self.liquidation_mark = ut.OKEX_NO      # 强平标志,默认是'NO'，强平信号出现时候标'YES',标'YES'之后就要执行强平，不再回退到'NO'状态
        self.liquidation_mark_time = datetime.now().strftime("%Y%m%d %H:%M:%S")  #统计时点时间       # 标志强退的时间点
        self.liquidation_complete = ut.OKEX_NO  # 跟踪是否已经完成了强平交易
        self.liquidation_complete_time = datetime.now().strftime("%Y%m%d %H:%M:%S")  #统计时点时间   # 强平交易完成时间点
        # self.update_date_time = datetime.utcnow()

        return None

    @staticmethod
    def tablename():
        return 'greed_mark'

    @staticmethod
    def primary_key_index():
        #第一个colum:contract_id是主键
        return [0, 3]

    @staticmethod
    def columns():
        """
        Return static columns names
        """
        return ['contract_id', 'exchange', 'time', 'long_or_short',
                'loss_scope', 'profit_scope', 'profit_liquidation_scope', 'amount',
                'last_profit_loss_ratio', 'now_profit_loss_ratio', 'top_profit_loss_ratio', 'bottom_profit_loss_ratio',
                'liquidation_mark', 'liquidation_mark_time', 'liquidation_complete', 'liquidation_complete_time']

    @staticmethod
    def types():
        """
        Return static column types
        """
        return ['text', 'varchar(20)', 'varchar(25)', 'varchar(10)',
                'decimal(10,5)', 'decimal(10,5)', 'decimal(10,5)', 'decimal(10,5)',
                'decimal(10,5)', 'decimal(10,5)', 'decimal(10,5)', 'decimal(10,5)',
                'varchar(10)', 'varchar(25)', 'varchar(10)', 'varchar(25)']

    def values(self):
        """
        Return values in a list
        """
        return [self.contract_id] + [self.exchange] + [self.time] + [self.long_or_short] + \
               [self.loss_scope] + [self.profit_scope] + [self.profit_liquidation_scope] + [self.amount] + \
               [self.last_profit_loss_ratio] + [self.now_profit_loss_ratio] + [self.top_profit_loss_ratio] + [self.bottom_profit_loss_ratio] + \
               [self.liquidation_mark] + [self.liquidation_mark_time] + [self.liquidation_complete] + [self.liquidation_complete_time]

    def print_detail(self, i=1):

        total_with = 10 + 16 * 15

        if i == 1:
            print('=' * total_with)
            format_tile = "%-10s%-20s%-20s%-15s" \
                          "%15s%15s%15s%15s" \
                          "%15s%15s%15s%15s" \
                          "%15s%20s%20s%20s"
            print(format_tile % ("No.", "contract_id", "time", "long_or_short",
                                 "loss_scope", "profit_scope", "liquid_scope", "amount",
                                 "top_profit", "bot_profit", "now_profit", "last_profit",
                                 "liquid_mark", "mark_time", "liquid_comp", "comp_time"
                                 ))
            print('-' * total_with)

        format_value = "%-10d%-20s%15s%15s" \
                       "%15.4f%15.4f%15.4f%15.4f" \
                       "%15.4f%15.4f%15.4f%15.4f" \
                       "%15s%25s%15s%25s"
        print(format_value % (
            i, self.contract_id, self.time, self.long_or_short,
            self.loss_scope, self.profit_scope, self.profit_liquidation_scope, self.amount,
            self.top_profit_loss_ratio, self.bottom_profit_loss_ratio, self.now_profit_loss_ratio, self.last_profit_loss_ratio,
            self.liquidation_mark, self.liquidation_mark_time, self.liquidation_complete, self.liquidation_complete_time
        ))


class GreedMarks:
    def __init__(self):
        self.GreedMarks_list = []
        self.db_client = SqliteClient()
        self.db_client.connect(path=ut.SQLPLITE_PATH)
        self.is_database_defined = True
        return None

    #插入并替换，根据主键替换
    def insert_greedmark_to_database(self, greedmark):
        self.db_client.insert(greedmark.tablename(), greedmark.columns(), greedmark.types(), greedmark.values(),
                              greedmark.primary_key_index(), True)

    def delete_greedmark_from_database(self, contract_id):
        #self.db_client.insert(greedmark.tablename(), greedmark.columns(), greedmark.types(), greedmark.values())
        pass

    def update_greedmark_from_database(self, greedmark):
        #self.db_client.insert(greedmark.tablename(), greedmark.columns(), greedmark.types(), greedmark.values())
        pass

    def select_greedmark_from_database(self, contract_id, long_or_short, liquidation_mark):
        greed_mark_get = GreedMark()
        sqlcon = "contract_id='%d' and long_or_short='%s' and liquidation_mark='%s'" \
                 % (contract_id, long_or_short, liquidation_mark)
        #print(sqlcon)
        select_result = self.db_client.select(greed_mark_get.tablename(), greed_mark_get.columns(), sqlcon)
        '''
        [('201809280020041', 'OkEx', '20180918 20:55:27', -0.2, 0.2, 0.2, 0, 0, 66.17, 66.17, 'NO', '20180918 20:55:27', 'NO', '20180918 20:55:27')]
        '''
        #print(select_result)

        for obj in select_result:
            greed_mark = GreedMark()
            greed_mark.contract_id = obj[0]
            greed_mark.exchange = obj[1]
            greed_mark.time = obj[2]
            greed_mark.long_or_short = obj[3]
            greed_mark.loss_scope = float(obj[4])
            greed_mark.profit_scope = float(obj[5])  # 最低盈利幅度，超过此盈利幅度才考虑止盈强平
            greed_mark.profit_liquidation_scope = float(obj[6])  # 盈利情况下，强平回调比例，0.2表示比盈利最高点回调20%的时候强平止盈

            greed_mark.last_profit_loss_ratio = float(obj[7])  # 最近的上一次查询的盈亏比率
            greed_mark.now_profit_loss_ratio = float(obj[8])  # 现在查询的“盈亏比率”
            greed_mark.top_profit_loss_ratio = float(obj[9])  # 表示“盈亏比率”曾经达到的最高点
            greed_mark.bottom_profit_loss_ratio = float(obj[10])  # 表示“盈亏比率”曾经达到的最低点

            greed_mark.liquidation_mark = obj[11]  # 强平标志,默认是'NO'，强平信号出现时候标'YES',标'YES'之后就要执行强平，不再回退到'NO'状态
            greed_mark.liquidation_mark_time = obj[12]  # 统计时点时间       # 标志强退的时间点
            greed_mark.liquidation_complete = obj[13]  # 跟踪是否已经完成了强平交易
            greed_mark.liquidation_complete_time = obj[14]  # 统计时点时间   # 强平交易完成时间点
            return greed_mark
        return None

    def add_greedmark(self, greedmark):
        self.GreedMarks_list.append(greedmark)

    def add_greedmarks(self, greedmarks):
        if len(greedmarks.Positions_list) > 0:
            self.GreedMarks_list.extend(greedmarks.Positions_list)

    def get_greedmark(self, contract_id, long_or_short=ut.OKEX_LONG, liquidation_mark=ut.OKEX_NO):
        for greedmark in self.GreedMarks_list:
            if greedmark.contract_id == contract_id and greedmark.long_or_short == long_or_short and \
                    greedmark.liquidation_mark == liquidation_mark:
                return greedmark
        return None

    def print_detail(self):
        if len(self.GreedMarks_list) == 0:
            return
        i = 1
        for greedmark in self.GreedMarks_list:
            greedmark.print_detail(i)
            i = i + 1
