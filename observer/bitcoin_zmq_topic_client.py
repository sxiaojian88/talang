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

import sys
import time

import zmq
import numpy
import json

def main():
    '''
    if len (sys.argv) < 2:
        print('usage: subscriber <connect_to> [topic topic ...]')
        sys.exit (1)

    connect_to = sys.argv[1]
    topics = sys.argv[2:]
    '''
    connect_to ='tcp://119.28.51.224:5001'
    topics = [
              b'HuoBiProTalang.BTCUSDT', b'HuoBiProTalang.EOSUSDT', b'HuoBiProTalang.EOSBTC',
              b'HuoBiProTalang.ETHUSDT', b'HuoBiProTalang.EOSETH', b'HuoBiProTalang.ETHBTC',
              b'OkExRestTalang.EOSUSDT', b'OkExRestTalang.ETHUSDT', b'OkExRestTalang.BTCUSDT',
              b'OkExRestTalang.EOSBTC', b'OkExRestTalang.ETHBTC', b'OkExRestTalang.EOSETH',
              b'Binance.BTCUSDT',
              b'Binance.ETHBTC', b'Binance.EOSETH', b'Binance.EOSBTC'
            ]#,b'HuoBi.BTCUSDT']#,b'Okex.BTC',b'Bitfinex.BTCUSD',b'sports.general']

    '''
    BC_MC=EOSBTC
    QC_MC=ETHBTC
    BC_QC=EOSETH
    '''
    ctx = zmq.Context()
    s = ctx.socket(zmq.SUB)
    s.connect(connect_to)

    # manage subscriptions
    if not topics:
        print("Receiving messages on ALL topics...")
        s.setsockopt(zmq.SUBSCRIBE,'')
    else:
        print("Receiving messages on topics: %s ..." % topics)
        for t in topics:
            s.setsockopt(zmq.SUBSCRIBE,t)
    print
    BC_MC_buy_1_price = 0
    BC_MC_sell_1_price = 0
    QC_MC_buy_1_price = 0
    QC_MC_sell_1_price = 0
    BC_QC_buy_1_price = 0
    BC_QC_sell_1_price = 0
    try:
        while True:
            topic, msg = s.recv_multipart()
            print('   Topic: %s, msg:%s' % (topic, msg))
            msg=bytes.decode(msg)
            msg=eval(msg)
            msg=dict(msg)


            if msg['instmt']=='EOSBTC' :
                BC_MC_buy_1_price=float(msg['b1'])
                BC_MC_sell_1_price=float(msg['a1'])
            elif msg['instmt']=='ETHBTC' :
                QC_MC_buy_1_price=float(msg['b1'])
                QC_MC_sell_1_price=float(msg['a1'])
            elif msg['instmt']=='EOSETH' :
                BC_QC_buy_1_price=float(msg['b1'])
                BC_QC_sell_1_price=float(msg['a1'])


            if QC_MC_sell_1_price*BC_QC_sell_1_price != 0 :
                print(BC_MC_buy_1_price/(QC_MC_sell_1_price*BC_QC_sell_1_price)-1)
            else:
                print('QC_MC_sell_1_price*BC_QC_sell_1_price:0')

            if QC_MC_buy_1_price*BC_QC_buy_1_price != 0:
                print(1-BC_MC_sell_1_price/(QC_MC_buy_1_price*BC_QC_buy_1_price))
            else:
                print('QC_MC_buy_1_price*BC_QC_buy_1_price:0')

            '''
            BC_MC=EOSBTC
            QC_MC=ETHBTC
            BC_QC=EOSETH
            '''
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
            #print(msg['trade_px'])

    except KeyboardInterrupt:
        pass
    print("Done.")


if __name__ == "__main__":
    main()
