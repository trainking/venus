#coding: utf-8

def k_chart_data(code):
    """
        根据code获取K线图数据
        Args:
            code：股票代码
        Returns:
            [] 股票收盘价数据
    """
    data = ts.get_hist_data(code)
    r = data.close
    return [
            (x,r[x]) for x in r.index
        ]
