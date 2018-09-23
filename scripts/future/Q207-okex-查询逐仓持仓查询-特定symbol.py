#!/usr/bin/env python

import talang.manage.account.future_position_4fix_service as future_position_4fix_service
import talang.util.model.Position as position_model

def main():

    #===============输入参数=======================
    symbol = 'xrp_usd'
    contractType = 'this_week'
    type1 = 1
    # =============================================
    positionFixSer = future_position_4fix_service.FuturePositionFixService()
    okex_positions = positionFixSer.get_positions_okex(symbol, contractType, type1)
    #okex_positions = positionFixSer.get_positions_okex_all()
    okex_positions.print_detail()

    #插入到数据库中
    '''
    position_database = position_model.PositionDatabase()
    for position in okex_positions.Positions_list:
        position_database.insert_position_to_database(position)
    '''



if __name__ == "__main__":
    main()
