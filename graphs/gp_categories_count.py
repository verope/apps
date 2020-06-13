from app import app

import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go

import numpy as np
import pandas as pd


data = pd.read_csv("/Users/veronikapeskova/projects/portfolio/plotly_dash/apps_app/apps/data/category.csv")


bar_data = [
    go.Bar(
        y=data['Category'].value_counts().sort_values().to_dense().keys(),
        x=data['Category'].value_counts().sort_values(),
        orientation='h',
        text="Number of Apps in Category",
    )]
layout = go.Layout(
    height=800,
    title='Number of Apps in each category',
    hovermode='closest',
    yaxis=dict(title='Category', gridwidth=2, domain=[0.1, 1]),
    showlegend=False
)
fig = go.Figure(data=bar_data, layout=layout)

graph = html.Div(
    [
        dcc.Graph(
            id='my-graph',
            figure=fig
        )
    ]
)
