import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import datetime as dt
import datetime
import plotly.graph_objs as go

app = dash.Dash(__name__)
server = app.server
app.config.suppress_callback_exceptions = True

from pages import homepage

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return homepage.layout
    else:
        return '404'

# register callbacks here:

if __name__ == '__main__':
    app.run_server(debug=True)