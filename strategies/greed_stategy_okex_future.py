import talang.exchanges.okex.util as okex_util
import talang.util.util_data as ut
import talang.util.model.Position as position_model
import talang.util.model.GreedMark as greed_mark_model
import time
from datetime import datetime
import talang.manage.account.future_position_4fix_service as future_position_4fix_service
import talang.trader.trade.future_trade_service as future_trade_service
# 期货API
okcoinFuture = okex_util.getOkcoinFuture()

    

class GreedStrategyOkexFutureService:
    def __init__(self):
        self.monitor_period = 5  # 监测周期，5表示每秒监测一次
        self.greed_marks = greed_mark_model.GreedMarks()

        return None

    #监控并对满足条件的进行强平标识
    def do_liquidation_mark(self):
        position_fix_service = future_position_4fix_service.FuturePositionFixService()
        trade_service = future_trade_service.FutureTradeService()
        
        okex_positions = position_fix_service.get_positions_okex_all()
        okex_positions.print_detail()
        i = 1
        for position in okex_positions.Positions_list:
            new_greed_mark = False
            #根据contract_id查询是否已有
            #greedmark = self.greed_marks.get_greedmark(position.contract_id)
            greedmark = self.greed_marks.select_greedmark_from_database(position.contract_id)

            if greedmark == None:
                new_greed_mark = True
                greedmark = greed_mark_model.GreedMark()
                greedmark.exchange = ut.okex_exchange
                greedmark.time = datetime.now().strftime("%Y%m%d %H:%M:%S")  #统计时点时间
                greedmark.contract_id = position.contract_id
                if position.LongOrShort() == ut.OKEX_LONG:
                    greedmark.top_profit_loss_ratio = position.buy_profit_lossratio
                    greedmark.bottom_profit_loss_ratio = position.buy_profit_lossratio
                elif position.LongOrShort() == ut.OKEX_SHORT:
                    greedmark.top_profit_loss_ratio = position.sell_profit_lossratio
                    greedmark.bottom_profit_loss_ratio = position.sell_profit_lossratio

            greedmark.last_profit_loss_ratio = greedmark.now_profit_loss_ratio
            if position.LongOrShort() == ut.OKEX_LONG:
                greedmark.now_profit_loss_ratio = position.buy_profit_lossratio
            elif position.LongOrShort() == ut.OKEX_SHORT:
                greedmark.now_profit_loss_ratio = position.sell_profit_lossratio

            if greedmark.now_profit_loss_ratio > greedmark.top_profit_loss_ratio:
                greedmark.top_profit_loss_ratio = greedmark.now_profit_loss_ratio
            if greedmark.now_profit_loss_ratio < greedmark.bottom_profit_loss_ratio:
                greedmark.bottom_profit_loss_ratio = greedmark.now_profit_loss_ratio

            if greedmark.now_profit_loss_ratio < greedmark.loss_scope or \
                    (greedmark.now_profit_loss_ratio < greedmark.top_profit_loss_ratio * (1- greedmark.profit_liquidation_scope) and \
                     greedmark.now_profit_loss_ratio > greedmark.profit_scope ):
                greedmark.liquidation_mark = ut.OKEX_YES
                greedmark.liquidation_mark_time = datetime.now().strftime("%Y%m%d %H:%M:%S")  #统计时点时间

                trade_service.liquidate_4fix_position(position)

            # add and update greedmark
            #if new_greed_mark == True:
            self.greed_marks.insert_greedmark_to_database(greedmark)
            greedmark.print_detail(i)
            i = i + 1


        return ''



    #对满足强平标志的进行强平
    def do_liuqdation(self):

        return

if __name__ == "__main__":

    greed_strategy_service = GreedStrategyOkexFutureService()
    while True:
        greed_strategy_service.do_liquidation_mark()
        time.sleep(10)