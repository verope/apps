import dash_html_components as html
import dash_core_components as dcc

page_logo = html.Div(
    [
        html.Img(
            src='https://cmsphoto.ww-cdn.com/superstatic/41269/art/grande/5297951-7905525.jpg?v=1558361891'
        )
    ], className='page-logo')

page_title = html.Div(
    [
        html.H1('Google Play & App Store Analysis')
    ], className='page-title')

navbar = html.Nav(
    [
        html.A('Homepage', href="/",
               className="nav-button"),
        html.A('App Store', href="/",
               className="nav-button"),
        html.A('Google Play', href="/",
               className="nav-button"),
    ], className="navbar"
)

layout = html.Div(
    [
        html.Div(
            [
                page_logo,
                page_title,
                navbar
            ], className="navbar"),
        html.Div(
            [
                "Hello"
            ], className="filter__container"
        )
    ]
)
