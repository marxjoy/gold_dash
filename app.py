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

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

df = pd.read_pickle('curr_and_gold.p')

codes = ['USD', 'AUD', 'CAD', 'EUR', 'HUF', 'CHF', 'GBP', 'JPY', 'CZK',
       'DKK', 'NOK', 'SEK', 'XDR', 'EEK', 'GOLD']

colors = ['firebrick', 'blue', 'red', 'gold', 'grey', 'silver', 'crimson', 'pink', 'yellow', 'lime', 'aqua', 'salmon','brown', 'purple', 'grey', 'magenta', 'violet']

fig = go.Figure()
for i, code in enumerate(codes):
    res = df[df.code == code]
    #fig = px.scatter(res, x="date", y="bid")
    fig.add_trace(go.Scatter(x=res.date, y=res.bid, name=str(res.currency.iloc[0]),
                             line=dict(color=colors[i], width=3)))




# # Add data
# month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
#          'August', 'September', 'October', 'November', 'December']
# high_2000 = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
# low_2000 = [13.8, 22.3, 32.5, 37.2, 49.9, 56.1, 57.7, 58.3, 51.2, 42.8, 31.6, 15.9]
# high_2007 = [36.5, 26.6, 43.6, 52.3, 71.5, 81.4, 80.5, 82.2, 76.0, 67.3, 46.1, 35.0]
# low_2007 = [23.6, 14.0, 27.0, 36.8, 47.6, 57.7, 58.9, 61.2, 53.3, 48.5, 31.0, 23.6]
# high_2014 = [28.8, 28.5, 37.0, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]
# low_2014 = [12.7, 14.3, 18.6, 35.5, 49.9, 58.0, 60.0, 58.6, 51.7, 45.2, 32.2, 29.1]
#
# fig = go.Figure()
# # Create and style traces
# fig.add_trace(go.Scatter(x=month, y=high_2014, name='High 2014',
#                          line=dict(color='firebrick', width=4)))
# fig.add_trace(go.Scatter(x=month, y=low_2014, name = 'Low 2014',
#                          line=dict(color='royalblue', width=4)))
# fig.add_trace(go.Scatter(x=month, y=high_2007, name='High 2007',
#                          line=dict(color='firebrick', width=4,
#                               dash='dash') # dash options include 'dash', 'dot', and 'dashdot'
# ))
# fig.add_trace(go.Scatter(x=month, y=low_2007, name='Low 2007',
#                          line = dict(color='royalblue', width=4, dash='dash')))
# fig.add_trace(go.Scatter(x=month, y=high_2000, name='High 2000',
#                          line = dict(color='firebrick', width=4, dash='dot')))
# fig.add_trace(go.Scatter(x=month, y=low_2000, name='Low 2000',
#                          line=dict(color='royalblue', width=4, dash='dot')))
#
# # Edit the layout
# fig.update_layout(title='Average High and Low Temperatures in New York',
#                    xaxis_title='Month',
#                    yaxis_title='Temperature (degrees F)')


#fig.show()
###

fig.update_layout(clickmode='event+select')

fig.update_traces(marker_size=20)

app.layout = html.Div([
    dcc.Graph(
        id='basic-interactions',
        figure=fig
    ),
    ])






if __name__ == '__main__':
    app.run_server(debug=True)
