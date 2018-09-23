# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util
import talang.util.util_data as ut
import talang.util.model.Position as position_model
from datetime import datetime
from talang.util.Logger import Logger
# 期货API
okcoinFuture = okex_util.getOkcoinFuture()


class FutureTradeService:

    #插入到数据库表中记录起来
    def record_liquidate_4fix_position(self, position):
        print('liquidate_4fix_position:')
        position.print_detail(1)
        #插入到数据库表中
        position_database = position_model.PositionDatabase()
        position_database.insert_position_to_database(position)
        pass


    def do_liquidate_future_trade(self,position):
        return_msg = ut.OKEX_NO
        try:
            res = okcoinFuture.future_trade(position.symbol, position.contract_type, '', position.get_amount(),
                                            position.get_liquidate_trade_type(), '1', position.lever_rate)
            result = res["result"]
            #print('do_liquidate_future_trade result:%s' % result)

            if result == True:
                return_msg = ut.OKEX_YES
        except Exception as e:
            Logger.error('FutureTradeService', "do_liquidate_future_trade: %s" % e)

        return return_msg
