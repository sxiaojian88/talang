#!/usr/bin/env python
# -*- coding: utf-8 -*-


import marketHelper
# 设定账户 accountConfig
import traceback
import time
import logging
# import yaml
import multiprocessing
import math
from utils.helper import *

# 设置logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
main_log_handler = logging.FileHandler("log/triangle_main_{0}.log".format(int(time.time())), mode="w", encoding="utf-8")
main_log_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
main_log_handler.setFormatter(formatter)
logger.addHandler(main_log_handler)


class Triangle:
    """
        交易对：用一种资产（quote currency）去定价另一种资产（base currency）,比如用比特币（BTC）去定价莱特币（LTC），
        就形成了一个LTC/BTC的交易对，
        交易对的价格代表的是买入1单位的base currency（比如LTC）
        需要支付多少单位的quote currency（比如BTC），
        或者卖出一个单位的base currency（比如LTC）
        可以获得多少单位的quote currency（比如BTC）。
        当LTC对BTC的价格上涨时，同等单位的LTC能够兑换的BTC是增加的，而同等单位的BTC能够兑换的LTC是减少的。
    """
    def __init__(self, base_cur="ltc", quote_cur="btc", mid_cur="cny", interval=10):
        """
        初始化
        :param base_cur:  基准资产
        :param quote_cur:  定价资产
        :param mid_cur:  中间资产
        :param interval:  策略触发间隔
        """

        # 设定套利监控交易对
        self.BC = base_cur
        self.QC = quote_cur
        self.MC = mid_cur   # 中间货币，cny或者btc

        self.base_quote_slippage = 0.002  # 设定市场价滑点百分比
        self.base_mid_slippage = 0.002
        self.quote_mid_slippage = 0.002

        self.base_quote_fee = 0.002  # 设定手续费比例
        self.base_mid_fee = 0.002
        self.quote_mid_fee = 0.002

        self.order_ratio_base_quote = 0.5  # 设定吃单比例
        self.order_ratio_base_mid = 0.5

        # 设定监控时间
        self.interval = interval

        # 设定市场初始 ------------现在没有接口，人工转币，保持套利市场平衡--------------

        self.base_quote_quote_reserve = 0.0    # 设定账户最少预留数量,根据你自己的初始市场情况而定, 注意： 是数量而不是比例
        self.base_quote_base_reserve = 0.0
        self.quote_mid_mid_reserve = 0.0
        self.quote_mid_quote_reserve = 0.0
        self.base_mid_base_reserve = 0.0
        self.base_mid_mid_reserve = 0.0

        # 最小的交易单位设定
        self.min_trade_unit = 0.2   # LTC/BTC交易对，设置为0.2, ETH/BTC交易对，设置为0.02

        self.market_price_tick = dict()  # 记录触发套利的条件时的当前行情

    def strategy(self, data):   # 主策略
        # 检查是否有套利空间
        try:
            '''
            正循环套利条件
            BC_MC_buy_1_price/(QC_MC_sell_1_price*BC_QC_sell_1_price)>
            1+QC_MC_slippage+BC_QC_slippage+BC_MC_slippage+QC_MC_fee+BC_MC_fee+BC_QC_fee
            '''

            '''
            逆循环套利条件
            BC_MC_sell_1_price/(QC_MC_buy_1_price*BC_QC_buy_1_price)<
            1-QC_MC_slippage+BC_QC_slippage+BC_MC_slippage+QC_MC_fee+BC_MC_fee+BC_QC_fee
            '''


        except:
            logger.error(traceback.format_exc())

if __name__ == "__main__":
    triangle = Triangle()
    while True:
        triangle.strategy()
        time.sleep(triangle.interval)
