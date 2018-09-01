

#同一时间，统一symbol下的不同Kline
class KlinePair:
    def __init__(self):
        self.Symbol = ''
        self.type = ''          #时间序列类型，如1min,1hour,1day
        self.Exchange_a = ''
        self.Exchange_b = ''
        self.Time = 0
        self.Kline_a = 0.0
        self.Kline_b = 0.0


class KlinePairs:

    def __init__(self):
        self.klinepairs = []