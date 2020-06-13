import sys
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
sys.path.append("..") # Adds higher directory to python modules path.

# import graphs/tables here
from graphs.gp_ratings_dist import graph as g1
from graphs.gp_categories_count import graph as g2
from navbar import layout as navbar_layout

layout = html.Div(
    [
        navbar_layout,
        html.Div(
            [
                g1,
                g2
            ],
            className="graph__container"),
    ],
    className="layout-content__container"
)
