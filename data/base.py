#coding: utf-8

import tushare as ts

def k_chart_data(code):
    """
        根据code获取K线图数据
        Args:
            code：股票代码
        Returns:
            [] 股票收盘价数据
    """
    _data = ts.get_hist_data(code)
    r = _data.sort_index().close
    return [
            (x,r[x]) for x in r.index
        ]

def info(code):
    """
        根据code获取基本信息
        Args:
            code：股票代码
        Returns:
            {}
    """
    _data = ts.get_stock_basics()
    _item = dict(_data.loc[code])
    return _item
