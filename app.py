import json

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

import plotly.graph_objects as go


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

df = pd.read_csv('curr_and_gold.csv')

codes = ['USD', 'AUD', 'CAD', 'EUR', 'HUF', 'CHF', 'GBP', 'JPY', 'CZK',
       'DKK', 'NOK', 'SEK', 'XDR', 'EEK', 'GOLD']

colors = ['firebrick', 'blue', 'red', 'gold', 'grey', 'silver', 'crimson',
          'pink', 'yellow', 'lime', 'aqua', 'salmon','brown', 'purple', 'grey', 'magenta', 'violet']

fig = go.Figure()
for i, code in enumerate(codes):
    res = df[df.code == code]
    #fig = px.scatter(res, x="date", y="bid")
    fig.add_trace(go.Scatter(x=res.date, y=res.bid, name=str(res.currency.iloc[0]),
                             line=dict(color=colors[i], width=3)))

fig.update_layout(clickmode='event+select')

fig.update_traces(marker_size=20)

app.layout = html.Div([
    dcc.Graph(
        id='basic-interactions',
        figure=fig
    ),
    ])


if __name__ == "__main__":
  server.run(host='0.0.0.0', port=5000)
