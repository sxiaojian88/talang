#!/usr/bin/env python

import talang.manage.account.future_position_4fix_service as future_position_4fix_service


def main():

    #===============输入参数=======================
    symbol = 'eos_usd'
    contractType = 'quarter'
    type1 = 1
    # =============================================
    positionFixSer = future_position_4fix_service.FuturePositionFixService()
    okex_positions = positionFixSer.get_positions_okex(symbol, contractType, type1)
    #okex_positions = positionFixSer.get_positions_okex_all()
    okex_positions.print_detail()


if __name__ == "__main__":
    main()
