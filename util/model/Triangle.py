from talang.util.model.ModelBase import ModelBase
import talang.util.util_data as ut
import talang.data.quote.quote_ticker as quote_ticker

class Triangle(ModelBase):

    def __init__(self):
        self.base_coin = ''
        self.quote_coin = ''
        self.middle_coin = ''


        BC_MC_buy_1_price = 0
        BC_MC_sell_1_price = 0
        BC_MC_buy_1_volume = 0
        BC_MC_sell_1_volume =0
        QC_MC_buy_1_price = 0
        QC_MC_sell_1_price = 0
        QC_MC_buy_1_volume = 0
        QC_MC_sell_1_volume =0
        BC_QC_buy_1_price = 0
        BC_QC_sell_1_price = 0
        BC_QC_buy_1_volume = 0
        BC_QC_sell_1_volume =0


        self.right_direction = 0
        self.left_direction = 0

    def get_BC_MC(self):
        self.symbol = ut.get_symbol(self.exchange, self.base_coin, self.middle_coin)
        return self.symbol

    def get_QC_MC(self):
        self.symbol = ut.get_symbol(self.exchange, self.quote_coin, self.middle_coin)
        return self.symbol

    def get_BC_QC(self):
        self.symbol = ut.get_symbol(self.exchange, self.base_coin, self.quote_coin)
        return self.symbol

    def print_direecton(self, i , direct = ut.RIGHT_DIRECT):
        q_ticker = quote_ticker.QuoteTicker()
        format_value = "%-5d%-10s%20s" \
                       "%15s%15s%15s" \
                        "%15.4f%15.4f%15.4f" \
                        "%15.4f%15.4f"
        this_MC_USDT_price = q_ticker.get_usdt_value_by_coin(self.exchange, self.middle_coin)
        this_QC_USDT_price = q_ticker.get_usdt_value_by_coin(self.exchange, self.quote_coin)

        if str.lower(direct) == ut.RIGHT_DIRECT.lower():
            print(format_value % (i, self.exchange, self.time,
                              ut.get_symbol(ut.okex_exchange, self.base_coin, self.middle_coin),
                              ut.get_symbol(ut.okex_exchange, self.base_coin, self.quote_coin),
                              ut.get_symbol(ut.okex_exchange, self.quote_coin, self.middle_coin),
                              this_MC_USDT_price * self.BC_MC_buy_1_price * self.BC_MC_buy_1_volume,
                              this_QC_USDT_price * self.BC_QC_sell_1_price * self.BC_QC_sell_1_volume,
                              this_MC_USDT_price * self.QC_MC_sell_1_price * self.QC_MC_sell_1_volume,
                              self.right_direction, self.left_direction
                              ))
        else:
            print(format_value % (i, self.exchange, self.time,
                              ut.get_symbol(ut.okex_exchange, self.base_coin, self.middle_coin),
                              ut.get_symbol(ut.okex_exchange, self.base_coin, self.quote_coin),
                              ut.get_symbol(ut.okex_exchange, self.quote_coin, self.middle_coin),
                              this_MC_USDT_price * self.BC_MC_sell_1_price * self.BC_MC_sell_1_volume,
                              this_QC_USDT_price * self.BC_QC_buy_1_price * self.BC_QC_buy_1_volume,
                              this_MC_USDT_price * self.QC_MC_buy_1_price * self.QC_MC_buy_1_volume,
                              self.right_direction, self.left_direction
                              ))

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

    def print_detail_right_direction(self):
        q_ticker = quote_ticker.QuoteTicker()
        #tri.right_direction = tri.BC_MC_buy_1_price / (tri.QC_MC_sell_1_price * tri.BC_QC_sell_1_price) - 1
        self.triangle_list.sort(key=lambda x: x.right_direction, reverse=False)

        total_with = 5 + 8 + 16 + 3*10 + 2*12 + 3*12 + 3*16
        print('=' * total_with)
        format_tile = "%-5s%-8s%16s" \
                      "%10s%10s%10s%12s%12s" \
                      "%12s%12s%12s" \
                      "%16s%16s%16s"

        print(format_tile % ("No.", "Exch", "Time",
                             "BC_MC", "QC_MC", "BC_QC", "Right_direct", "Left_direct",
                             "BC_MC_buy1", "QC_MC_sell1", "BC_QC_sell1",
                             "BC_MC_buy1_val", "QC_MC_sell1_val", "BC_QC_sell1_val"
                             ))
        print('-' * total_with)
        format_value = "%-5d%-8s%16s" \
                       "%10s%10s%10s%10.4f%10.4f" \
                       "%12.6f%12.6f%12.6f" \
                       "%16.4f%16.4f%16.4f"
        i = 1
        this_MC = ''
        this_QC = ''
        last_MC = ''
        last_QC = ''
        for tri in self.triangle_list:
            this_MC = tri.middle_coin
            this_QC = tri.quote_coin
            if str.lower(this_MC) != str.lower(last_MC):
                this_MC_USDT_price = q_ticker.get_usdt_value_by_coin(tri.exchange, this_MC)
            if str.lower(this_QC) != str.lower(last_QC):
                this_QC_USDT_price = q_ticker.get_usdt_value_by_coin(tri.exchange, this_QC)
            print(format_value % (i, tri.exchange, tri.time,
                                  tri.get_BC_MC(), tri.get_QC_MC(), tri.get_BC_QC(), tri.right_direction, tri.left_direction,
                                  tri.BC_MC_buy_1_price, tri.QC_MC_sell_1_price, tri.BC_QC_sell_1_price,
                                  this_MC_USDT_price * tri.BC_MC_buy_1_price * tri.BC_MC_buy_1_volume,
                                  this_MC_USDT_price * tri.QC_MC_sell_1_price * tri.QC_MC_sell_1_volume,
                                  this_QC_USDT_price * tri.BC_QC_sell_1_price * tri.BC_QC_sell_1_volume))
            i = i+1
            last_MC = this_MC
            last_QC = this_QC
        print('=' * total_with)

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