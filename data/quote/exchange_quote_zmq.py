#!/usr/bin/env python
"""Simple example of publish/subscribe illustrating topics.

Publisher and subscriber can be started in any order, though if publisher
starts first, any messages sent before subscriber starts are lost.  More than
one subscriber can listen, and they can listen to  different topics.

Topic filtering is done simply on the start of the string, e.g. listening to
's' will catch 'sports...' and 'stocks'  while listening to 'w' is enough to
catch 'weather'.
"""

#-----------------------------------------------------------------------------
#  Copyright (c) 2010 Brian Granger, Fernando Perez
#
#  Distributed under the terms of the New BSD License.  The full license is in
#  the file COPYING.BSD, distributed as part of this software.
#-----------------------------------------------------------------------------
'''
从BitcoinexchangeFH项目的zmq行情服务获取数据
'''

import zmq
import talang.util.util_data as ut

connect_to = 'tcp://172.19.0.3:5001'


class ExchangeQuoteZmq:

    def get_buy_1_value(self,exchange,base_coin,quote_coin):
        ex_qt = ExchangeQuoteZmq()
        msg=ex_qt.get_msg(exchange,base_coin,quote_coin)
        buy_1_price = float(msg['b1'])

        return buy_1_price

    def get_sell_1_value(self,exchange,base_coin,quote_coin):
        ex_qt = ExchangeQuoteZmq()
        msg=ex_qt.get_msg(exchange,base_coin,quote_coin)
        sell_1_price = float(msg['a1'])

        return sell_1_price

    @classmethod
    def get_msg(cls,exchange,base_coin,quote_coin):
        #组合topic值
        ex_qt = ExchangeQuoteZmq()
        topic = ex_qt.get_topic(exchange,base_coin,quote_coin)
        ctx = zmq.Context()
        s = ctx.socket(zmq.SUB)
        s.connect(connect_to)
        s.setsockopt(zmq.SUBSCRIBE, topic)
        topic_rec, msg = s.recv_multipart()
        #print('   Topic: %s, msg:%s' % (topic_rec, msg))
        msg = bytes.decode(msg)
        msg = eval(msg)
        msg = dict(msg)
        return msg

    @classmethod
    def get_topic(cls,exchange,base_coin,quote_coin):
        #组合topic值
        if ut.okex_exchange.lower() == exchange.lower() :
            topic = 'OkExRestTalang.' + base_coin.upper() + quote_coin.upper()
        else:
            topic = 'HuoBiProTalang.' + base_coin.upper() + quote_coin.upper()
        '''
        elif ut.huobipro_exchange.lower() == exchange.lower() :
            topic = 'HuoBiProTalang.' + base_coin.upper() + quote_coin.upper()
        else :
            return None
        '''
        return topic.encode()

if __name__ == '__main__':
    ex_qt=ExchangeQuoteZmq()
    exchange_name = 'okex'
    base_coin = 'EOS'
    quote_coin = 'BTC'
    buy_1=ex_qt.get_buy_1_value(exchange_name,base_coin,quote_coin)
    print("exchange_quote get buy_1:%f" % buy_1)