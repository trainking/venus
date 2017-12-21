# venus

A股证券分析，数据来源于Tushare。经过测试Tushare数据实时性不好，只能做历史性研究。

可视化使用`plotly`的`Dash`来做。

## 安装

Tushare:

```
pip install tushare
```

Dash:

```
pip install dash==0.19.0  # The core dash backend
pip install dash-renderer==0.11.1  # The dash front-end
pip install dash-html-components==0.8.0  # HTML components
pip install dash-core-components==0.15.2  # Supercharged components
pip install plotly --upgrade  # Plotly graphing library used in examples
```
