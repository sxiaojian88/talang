#!/bin/python
from datetime import datetime


class ModelBase:
    def __init__(self):
        self.exchange = ''          #此账号所属交易所，如果是所有交易所总和统计，以ALL表示
        self.time = datetime.now().strftime("%Y%m%d %H:%M:%S.%f")  #统计时点时间