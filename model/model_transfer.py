'''
在不同的相近模式（model）之间进行转换
'''
from befh.market_data import L2Depth
from talang.model.Depth import Depth


def l2depth_to_depth(l2depth):
    depth = Depth()
    depth.date_time = l2depth.date_time
    depth.bids = [e.copy() for e in l2depth.bids]
    depth.asks = [e.copy() for e in l2depth.asks]
    return depth
