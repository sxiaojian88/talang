from talang.util.model.ModelBase import ModelBase
import talang.util.util_data as ut


class Triangle(ModelBase):

    def __init__(self):
        self.base_coin = ''
        self.quote_coin = ''
        self.middle_coin = ''
        self.right_direction = 0
        self.left_direction = 0

    def get_BC_MC(self):
        self.symbol = ut.get_symbol(self.base_coin, self.middle_coin)
        return self.symbol

    def get_QC_MC(self):
        self.symbol = ut.get_symbol(self.quote_coin, self.middle_coin)
        return self.symbol

    def get_BC_QC(self):
        self.symbol = ut.get_symbol(self.base_coin, self.quote_coin)
        return self.symbol


class Triangles:
    def __init__(self):
        self.triangle_list = []

    def add_triangle(self, triangle):
        self.triangle_list.append(triangle)

    def sort_by_base_coin(self):
        self.triangle_list.sort(key=lambda x: x.base_coin, reverse=False)

    def sort_by_quote_coin(self):
        self.triangle_list.sort(key=lambda x: x.quote_coin, reverse=False)

    def sort_by_middle_coin(self):
        self.triangle_list.sort(key=lambda x: x.middle_coin, reverse=False)

    def sort_by_right_direction(self):
        self.triangle_list.sort(key=lambda x: x.right_direction, reverse=False)

    def sort_by_left_direction(self):
        self.triangle_list.sort(key=lambda x: x.left_direction, reverse=False)

    def print_detail(self):
        total_with = 6*15 + 5 + 18*2
        print('=' * total_with)
        format_tile = "%-5s%-10s%20s" \
                      "%15s%15s%15s" \
                      "%18s%18s"
        print(format_tile % ("No.", "Exchange", "Time",
                             "Base_Coin", "Quote_Coin", "Middle_Coin",
                             "Right_direction", "Left_direction"))
        print('-' * total_with)
        format_value = "%-5d%-10s%20s" \
                       "%15s%15s%15s" \
                       "%15.4f%15.4f"
        i = 1
        for tri in self.triangle_list:
            print(format_value % (i, tri.exchange, tri.time,
                                  tri.base_coin, tri.quote_coin, tri.middle_coin,
                                  tri.right_direction, tri.left_direction))
            i = i+1
        print('=' * total_with)