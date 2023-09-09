from dash import Dash, dcc, html, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Bootstrap/Side-Bar/iranian_students.csv')

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# styling the sidebar
SIDEBAR_SYTLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE ={
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = dbc.Card([
    dbc.CardBody([
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P(
            "Number of students per education level", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Page 1", href="/", active="exact"),
                dbc.NavLink("Page 2", href="/page=2", active="exact"),
                dbc.NavLink("Page 3", href="/page=3", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ])
], color="light", style={"hegith":"100vh",
                         "width":"16rem",
                         "position":"fixed"})