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

def border(code, day=None):
    """
       根据code价格区间，最大值以及最小值
        Args:
            code：股票代码
        Returns:
            () 第一个参数最小值，第二个参数最大值
    """
    _d = ts.get_hist_data(code)
    _c = None
    if day is not None:
        _c = _d.close[-day:]
    else:
        _c = _d.close
    return (round(_c.min(), 2), round(_c.max(), 2))
