#coding: utf-8

import tushare as ts
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

df = ts.get_stock_basics()

app = dash.Dash()
app.layout = html.Div(children=[
    html.H1(children="PE"),
    html.Div(children='''2017年'''),
    dcc.Graph(
        id = 'pe-graph',
        figure={
            'data': [go.Bar(x=df.head(50)['name'].values, y=df.head(50)['pe'].values, name='PE')],
            'layout': go.Layout(title='PE排名')
        }
    )
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
