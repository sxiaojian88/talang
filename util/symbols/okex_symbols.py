#!/usr/bin/env python

def main():
    p_str=['\
    STORJ_BTC','\
    TOPC_BTC','\
    XRP_BTC','\
    QUN_BTC','\
    STORJ_USDT','\
    TOPC_USDT','\
    XRP_USDT','\
    QUN_USDT']

    for spotname in p_str:
        a=spotname.strip()
        b=a.replace('_','')
        print('[OkExRestTalang-'+ a + '-Restful]\r\n'\
        +'exchange = OkExRestTalang\r\n'\
        +'instmt_name = '+ b+'\r\n'\
        +'instmt_code = '+ a+'\r\n'\
        +'enabled = 1\r\n')

    '''
    [OkExRestTalang-ETHUSDT-Restful]
    exchange = OkExRestTalang
    instmt_name = ETHUSDT
    instmt_code = ETH_USDT
    enabled = 1
    '''
if __name__ == "__main__":
    main()
