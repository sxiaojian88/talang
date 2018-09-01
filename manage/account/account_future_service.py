# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util
import talang.data.quote.quote_ticker as quote_ticker
import talang.util.util_data as ut
import talang.util.model.AccountFuture as acct_future


# 期货API
okcoinFuture = okex_util.getOkcoinFuture()


class AccountFutureService():
    """
    "info": {
        "btc": {
            "account_rights": 1,
            "keep_deposit": 0,
            "profit_real": 3.33,
            "profit_unreal": 0,
            "risk_rate": 10000
        },
        "ltc": {
            "account_rights": 2,
            "keep_deposit": 2.22,
            "profit_real": 3.33,
            "profit_unreal": 2,
            "risk_rate": 10000
        }
    },
    "result": true
    """

    def get_account_by_exchange(self, exchange):
        return "ok"

    def get_all_symbols_btc_usdt_cny(self):
        return "ok"

    def get_account_huobipro(self):

        return "ok"

    def get_account_okex(self):
        q_ticker = quote_ticker.QuoteTicker()
        res = okcoinFuture.future_userinfo()
        print(res)
        result = res["result"]
        
        info = res["info"]
        cur_keys = list(info.keys())
        total_btc = 0.0
        total_usdt = 0.0

        okex_account_future = acct_future.AccountFuture()
        okex_account_future.exchange = ut.okex_exchange

        for cur in cur_keys:
            cur_info = info[cur]

            okex_balance_future = acct_future.BalanceFuture()
            okex_balance_future.currency = cur
            okex_balance_future.account_rights = float(cur_info['account_rights'])
            okex_balance_future.keep_deposit = float(cur_info['keep_deposit'])
            okex_balance_future.profit_real = float(cur_info['profit_real'])
            okex_balance_future.profit_unreal = float(cur_info['profit_unreal'])
            okex_balance_future.risk_rate = float(cur_info['risk_rate'])

            btc_value = float(q_ticker.get_btc_value_by_coin(ut.okex_exchange, cur))
            usdt_value = float(q_ticker.get_usdt_value_by_coin(ut.okex_exchange, cur))

            total_num = okex_balance_future.account_rights + okex_balance_future.profit_real + okex_balance_future.profit_unreal

            t_btc_value = total_num * btc_value
            t_usdt_value = total_num * usdt_value
            total_btc = total_btc + t_btc_value
            total_usdt = total_usdt + t_usdt_value
            # print("currency:"+cur+",free:%f" % fre+",frozen:%f" % frd+",borrow:%f" % bor +",btc_value:%f" % t_btc_value + ",usdt_value:%f" % t_usdt_value +"(usdt_price:%f)" %usdt_value )

            okex_balance_future.btc_worth = t_btc_value
            okex_balance_future.btc_price = btc_value
            okex_balance_future.usdt_worth = t_usdt_value
            okex_balance_future.usdt_price = usdt_value
            okex_balance_future.cny_worth = float(q_ticker.get_cny_value(t_usdt_value))
            okex_balance_future.cny_price = float(q_ticker.get_cny_value(usdt_value))
            okex_account_future.add_balance(okex_balance_future)

        # print("-----------------------------------------------------------------------------")
        # print("total_btc:%f" %total_btc + ",total_usdt:%f" %total_usdt + ",total_cny:%f" %self.get_cny_value(total_usdt) )
        okex_account_future.total_usdt = total_usdt
        okex_account_future.total_btc = total_btc
        okex_account_future.total_cny = q_ticker.get_cny_value(total_usdt)
        okex_account_future.sort_balance()
        okex_account_future.cal_ccupy()

        return okex_account_future

    def get_account_zb(self):

        return "ok"


if __name__ == "__main__":
    act = AccountFutureService()
    okex_account = act.get_account_okex()
    okex_account.print_detail()
