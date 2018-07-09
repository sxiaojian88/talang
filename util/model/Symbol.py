from talang.util.model.ModelBase import ModelBase
import talang.util.util_data as ut


class Symbol(ModelBase):

    def __init__(self):
        self.base_coin = ''
        self.quote_coin = ''
        self.symbol = ''

    def get_symbol(self):
        self.symbol = ut.get_symbol(self.base_coin, self.quote_coin)
        return self.symbol


class Symbols:
    def __init__(self):
        self.symbols_list = []

    def add_symbol(self,symbol):
        self.symbols_list.append(symbol)

    def sort_by_base_coin(self):
        self.symbols_list.sort(key=lambda x: x.base_coin, reverse=False)

    def sort_by_quote_coin(self):
        self.symbols_list.sort(key=lambda x: x.quote_coin, reverse=False)

    def sort_by_symbol(self):
        self.symbols_list.sort(key=lambda x: x.symbol, reverse=False)

    def print_detail(self):
        total_with = 6*15 +5
        print('=' * total_with)
        format_tile = "%-5s%-10s%20s" \
                      "%15s%15s%15s"
        print(format_tile % ("No.", "Exchange", "Time",
                             "Base_Coin", "Quote_Coin", "Symbol"))
        print('-' * total_with)
        format_value = "%-5d%-10s%20s" \
                       "%15s%15s%15s"
        i = 1
        for syb in self.symbols_list:
            print(format_value % (i, syb.exchange, syb.time,
                                  syb.base_coin, syb.quote_coin ,syb.symbol))
            i = i+1
        print('=' * total_with)