#coding: utf-8

from flask import Flask
from flask import render_template
import json
import tushare as ts
import time
from data import *

app = Flask(__name__)

WEB_SITE = "http://localhost:8050"

@app.route("/")
def index():
    return render_template('index.html', site=WEB_SITE)

@app.route("/kchart/code/<code>")
def kchart(code):
    """
        K线图
    """
    return json.dumps(base.k_chart_data(code))

@app.route("/data/base/<code>")
def baseData(code):
    """
        基本面数据
    """
    _item = base.info(code)

    return json.dumps(_item)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=True)
