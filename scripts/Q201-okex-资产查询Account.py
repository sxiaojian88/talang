#!/usr/bin/env python
import talang.manage.account.account_zmq as act_zmq
import talang.manage.account.account_api as act_api


def main():

    #act = act_zmq.account_zmq()

    #以Tiker行情数据计算okex资产
    act = act_api.AccountApi()
    okex_account = act.get_account_okex()
    okex_account.print_detail()


if __name__ == "__main__":
    main()
