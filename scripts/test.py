
import talang.util.util_data as ut

def main():

   #bc = ut.get_base_coin("okex",'BTC_USDT')
   #print(bc)

   format_tile = "%-5s%-8s%16s" \
                 "%10s%10s%10s%10s" \
                 "%12s%12s%12s" \
                 "%18s%18s%18s"

   print(format_tile % ("No.", "Exch", "Time",
                        "BC_MC", "QC_MC", "BC_QC", "Right_direct",
                        "BC_MC_buy1", "QC_MC_sell1", "BC_QC_sell1",
                        "BC_MC_buy1_val", "QC_MC_sell1_val", "BC_QC_sell1_val"
                        ))
if __name__ == "__main__":
    main()
