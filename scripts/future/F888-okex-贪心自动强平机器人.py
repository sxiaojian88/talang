#!/usr/bin/env python
from talang.util.Logger import Logger
import talang.strategies.greed_stategy_okex_future as greed_stategy_okex_future_service
import time


def main():

    #===============输入参数=======================
    # 无
    # =============================================
    greed_strategy_service = greed_stategy_okex_future_service.GreedStrategyOkexFutureService()
    while True:
        try:
            greed_strategy_service.do_liquidation_mark()
        except Exception as e:
            #Logger.error('greed_strategy_service', "do_liquidation_mark: %s" % e)
            time.sleep(50)
            pass
        time.sleep(10)


if __name__ == "__main__":
    main()
