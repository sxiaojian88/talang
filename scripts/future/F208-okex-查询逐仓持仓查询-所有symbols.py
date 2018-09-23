#!/usr/bin/env python

import talang.manage.account.future_position_4fix_service as future_position_4fix_service


def main():

    #===============输入参数=======================
    # 无
    # =============================================
    positionFixSer = future_position_4fix_service.FuturePositionFixService()
    okex_positions = positionFixSer.get_positions_okex_all()
    okex_positions.print_detail()


if __name__ == "__main__":
    main()
