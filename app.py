#coding: utf-8

from flask import Flask
from flask import render_template
import json
import tushare as ts
import time

app = Flask(__name__)

WEB_SITE = "http://localhost:8050"

@app.route("/")
def index():
    return render_template('index.html', site=WEB_SITE)

@app.route("/kchart/code/<code>")
def kchart(code):
    data = ts.get_hist_data(code)
    r = data.close  # 获取收盘价的Series
    return json.dumps([
            (time.mktime(time.strptime(x, "%Y-%m-%d")),r[x]) for x in r.index
        ])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8050, debug=True)
