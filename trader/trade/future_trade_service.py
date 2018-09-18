# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util
import talang.util.util_data as ut
import talang.util.model.Position as fut_position
from datetime import datetime

# 期货API
okcoinFuture = okex_util.getOkcoinFuture()


class FutureTradeService:

    #将某个position按照市价强平
    def liquidate_4fix_position(self, position):
        print('liquidate_4fix_position:')
        position.print_detail(1)
        return 'ok'
