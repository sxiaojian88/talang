# -*- coding: utf-8 -*-
import talang.exchanges.okex.util as okex_util
import talang.util.util_data as ut
import talang.util.model.Position as fut_position
from datetime import datetime
from talang.util.Logger import Logger
# 期货API
okcoinFuture = okex_util.getOkcoinFuture()


class FuturePositionFixService():

    def get_positions_okex_all(self):
        symbols = ut.OKEX_FUTURE_SYMBOLS                    #okex合约交易支持的所有symbols
        contract_types = ut.OKEX_FUTURE_CONTRACT_TYPES      #okex合约交易支持的所有周期类型
        positions_all = fut_position.Positions()

        for symbol in symbols:
            for contract_type in contract_types:
                futurepositionfixservice = FuturePositionFixService()
                positions = futurepositionfixservice.get_positions_okex(symbol, contract_type, '1')
                positions_all.add_positions(positions)

        return positions_all


    def get_positions_okex(self, symbol, contractType, type1):
        '''
        # Request
        POST https://www.okex.com/api/v1/future_position_4fix.do
        # Response
        {'result': True, 'holding': [
            {'buy_price_avg': 0, 'symbol': 'eth_usd', 'lever_rate': 10, 'buy_available': 0, 'contract_id': 201809210020060,
             'sell_risk_rate': '104.79', 'buy_amount': 0, 'buy_risk_rate': '1,000,000.00', 'profit_real': 0.00786862,
             'contract_type': 'next_week', 'sell_flatprice': '186.566', 'buy_bond': 0, 'sell_profit_lossratio': '4.79',
             'buy_flatprice': '0.000', 'buy_profit_lossratio': '0.00', 'sell_amount': 16, 'sell_bond': 0.09424238,
             'sell_price_cost': 169.775, 'buy_price_cost': 0, 'create_date': 1536571738000, 'sell_price_avg': 169.775,
             'sell_available': 16}]}
        '''

        try:
            res = okcoinFuture.future_position_4fix(symbol, contractType, type1)
            #print(res)
            result = res["result"]

            if not result:
                return None
        except Exception as e:
            Logger.error('FuturePositionFixService', "get_positions_okex: %s" % e)

        msg_holdings = res["holding"]


        positions = fut_position.Positions()

        for i in range(len(msg_holdings)):
            msg_holding = msg_holdings[i]

            position = fut_position.Position()
            position.buy_amount = float(msg_holding["buy_amount"])                                  # 多仓数量
            #有则添加，持仓中，有可能多空有其一，或者两者都有，则各分别添加，多空都有的情况下变为两条position加入
            if position.buy_amount > 0:
                position.exchange = ut.okex_exchange                                                    # 此账号所属交易所，如果是所有交易所总和统计，以ALL表示
                position.time = datetime.now().strftime("%Y%m%d %H:%M:%S")                           # 统计时点时间
                position.symbol = msg_holding['symbol']                                                 # btc_usd ltc_usd eth_usd etc_usd bch_usd
                position.lever_rate = msg_holding['lever_rate']                                         # 杠杆倍数
                position.contract_id = msg_holding['contract_id']                                       # 合约id
                position.contract_type = msg_holding['contract_type']                                   # 合约类型
                create_date = float(msg_holding["create_date"]) / 1000
                position.create_date = datetime.fromtimestamp(create_date).strftime("%Y%m%d %H:%M:%S")  # 创建日期
                position.profit_real = float(msg_holding["profit_real"])                                # 已实现盈余

                position.buy_profit_lossratio = float(msg_holding["buy_profit_lossratio"])              # 多仓盈亏比
                position.buy_available = float(msg_holding["buy_available"])                            # 多仓可平仓数量
                position.buy_bond = float(msg_holding["buy_bond"])                                      # 多仓保证金
                position.buy_price_avg = float(msg_holding["buy_price_avg"])                            # 多仓开仓平均价
                position.buy_flatprice = float(msg_holding["buy_flatprice"])                            # 多仓强平价格
                position.buy_price_cost = float(msg_holding["buy_price_cost"])                          # 多仓结算基准价
                position.buy_risk_rate = msg_holding["buy_risk_rate"]                           #

                positions.add_position(position)

            position_sell = fut_position.Position()
            position_sell.sell_amount = float(msg_holding["sell_amount"])                                # 空仓数量
            #有则添加，持仓中，有可能多空有其一，或者两者都有，则各分别添加，多空都有的情况下变为两条position加入
            if position_sell.sell_amount > 0:
                position_sell.exchange = ut.okex_exchange                                                    # 此账号所属交易所，如果是所有交易所总和统计，以ALL表示
                position_sell.time = datetime.now().strftime("%Y%m%d %H:%M:%S")                           # 统计时点时间
                position_sell.symbol = msg_holding['symbol']                                                 # btc_usd ltc_usd eth_usd etc_usd bch_usd
                position_sell.lever_rate = msg_holding['lever_rate']                                         # 杠杆倍数
                position_sell.contract_id = msg_holding['contract_id']                                       # 合约id
                position_sell.contract_type = msg_holding['contract_type']                                   # 合约类型
                create_date = float(msg_holding["create_date"]) / 1000
                position_sell.create_date = datetime.fromtimestamp(create_date).strftime("%Y%m%d %H:%M:%S")  # 创建日期
                position_sell.profit_real = float(msg_holding["profit_real"])                                # 已实现盈余

                position_sell.sell_profit_lossratio = float(msg_holding["sell_profit_lossratio"])            # 空仓盈亏比
                position_sell.sell_available = float(msg_holding["sell_available"])                          # 空仓可平仓数量
                position_sell.sell_bond = float(msg_holding["sell_bond"])                                    # 空仓保证金
                position_sell.sell_price_avg = float(msg_holding["sell_price_avg"])                          # 空仓开仓平均价
                position_sell.sell_flatprice = float(msg_holding["sell_flatprice"])                          # 空仓强平价格
                position_sell.sell_price_cost = float(msg_holding["sell_price_cost"])                        # 空仓结算基准价
                position_sell.sell_risk_rate = msg_holding["sell_risk_rate"]                          #

                positions.add_position(position_sell)

        return positions


if __name__ == "__main__":
    symbol = 'eos_usd'
    contractType = 'quarter'
    type1 = 1
    positionFixSer = FuturePositionFixService()
    #okex_positions = positionFixSer.get_positions_okex(symbol, contractType, type1)
    okex_positions = positionFixSer.get_positions_okex_all()
    okex_positions.print_detail()
