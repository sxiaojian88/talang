#!/bin/python
from datetime import datetime


class BalanceFuture:
    def __init__(self):
        self.currency = ''              # 币种名称
        self.account_rights = 0.0       # 账户权益
        self.keep_deposit = 0.0         # 保证金
        self.profit_real = 0.0          # 已实现盈亏
        self.profit_unreal = 0.0        # 未实现盈亏
        self.risk_rate = 0.0            # 保证金率

        self.btc_worth = 0.0    # 此币种以btc计价，总共价值多少
        self.btc_price = 0.0    # 此币种以btc计价，单价多少
        self.usdt_worth = 0.0   # 此币种以usdt计价，总共价值多少
        self.usdt_price = 0.0   # 此币种以usdt计价，单价多少
        self.cny_worth = 0.0    # 此币种以cny计价，总共价值多少
        self.cny_price = 0.0    # 此币种以cny计价，单价多少
        self.occupy = 0.0       # 此币种占此账号总资产占比多少（33.88百分制表示）


class AccountFuture:
    def __init__(self):
        self.exchange = ''          #此账号所属交易所，如果是所有交易所总和统计，以ALL表示
        self.time = datetime.now().strftime("%Y%m%d %H:%M:%S.%f")  #统计时点时间
        self.total_btc = 0.0        #所有资产以btc计价，总共价值多少
        self.total_usdt = 0.0       #所有资产以usdt计价，总共价值多少
        self.total_cny = 0.0        #所有资产以cny计价，总共价值多少
        self.balances = []          #保存Balance类型的列表

    def add_balance(self, balance):
        self.balances.append(balance)

    def cal_ccupy(self):
        if self.total_usdt == 0:
            return
        for balance in self.balances:
            balance.occupy = (balance.usdt_worth / self.total_usdt)*100

    def sort_balance(self):
        self.balances.sort(key=lambda x:x.usdt_worth, reverse=True)

    def print_detail(self):


        total_with = 12 + 5*15 + 6*15 + 10 + 10
        print('=' * (total_with))
        format_tile = "%-10s%-12s%15s%15s%15s%15s%15s%15s%15s%15s%15s%15s%15s%10s"
        print(format_tile % ("No.", "Currency", "account_rights", "keep_deposit", "profit_real", "profit_unreal",
                            "risk_rate",
                            "btc_price", "btc_worth", "usdt_price", "usdt_worth",
                            "cny_price", "cny_worth", "occupy(%)"))
        print('-' * total_with)
        format_value = "%-10d%-12s%15.8f%15.8f%15.8f%15.8f%15.8f%15.8f%15.8f%15.4f%15.4f%15.4f%15.4f%10.2f"
        i = 1
        for bl in self.balances:
            print(format_value %(i, bl.currency, bl.account_rights, bl.keep_deposit, bl.profit_real, bl.profit_unreal,
                                 bl.risk_rate,
                                 bl.btc_price, bl.btc_worth, bl.usdt_price, bl.usdt_worth,
                                 bl.cny_price, bl.cny_worth, bl.occupy))
            i = i + 1
        print('-' * total_with)
        print("exchange:%-12s"%self.exchange +"time:%-30s" % self.time \
              +"total_btc:%-15.4f" % self.total_btc + "total_usdt:%-15.4f" % self.total_usdt + "total_cny:%-15.4f" % self.total_cny)
        print('=' * total_with)


