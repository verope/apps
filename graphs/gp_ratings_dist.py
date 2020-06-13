from app import app

import dash_html_components as html
import dash_core_components as dcc
import plotly.figure_factory as ff

import numpy as np
import pandas as pd


data = pd.read_csv("/Users/veronikapeskova/projects/portfolio/plotly_dash/apps_app/apps/data/rating.csv")

x = data.Rating
hist_data = [x]
group_labels = ['Ratings Google']

fig = ff.create_distplot(hist_data, group_labels, bin_size=0.2)

graph = html.Div(
    [
        dcc.Graph(
            id='my-graph',
            figure=fig
        )
    ]
)
