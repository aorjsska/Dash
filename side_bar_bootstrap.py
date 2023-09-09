from dash import Dash, dcc, html, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Bootstrap/Side-Bar/iranian_students.csv')

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
# app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

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
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Page-1", href="/page-1", active="exact"),
                dbc.NavLink("Page-2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ])
], color="light", style={"hegith":"100vh",
                         "width":"16rem",
                         "position":"fixed"})

content = html.Div(id="page-content", style={"padding":"2rem"})

app.layout = dbc.Container([
    dcc.Location(id="url"),
    dbc.Row([
        dbc.Col(sidebar,width=2),
        dbc.Col(content,width=9,style={"margin-left":"16rem"})
    ])
], fluid=True)

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [
                html.H1('Kindergarten in Iran',
                        style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                         figure=px.bar(df, barmode='group', x='Years',
                         y=['Girls Kindergarten', 'Boys Kindergarten']))
                ]
    elif pathname == "/page-1":
        return [
                html.H1('Grad School in Iran',
                        style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                         figure=px.bar(df, barmode='group', x='Years',
                         y=['Girls Grade School', 'Boys Grade School']))
                ]
    elif pathname == "/page-2":
        return [
                html.H1('High School in Iran',
                        style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                         figure=px.bar(df, barmode='group', x='Years',
                         y=['Girls High School', 'Boys High School']))
                ]
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        dbc.Container(
            [
                html.H1("Jumbotron", className="display-3"),
                html.P(
                    "Use Containers to create a jumbotron to call attention to "
                    "featured content or information.",
                    className="lead",
                ),
                html.Hr(className="my-2"),
                html.P(
                    "Use utility classes for typography and spacing to suit the "
                    "larger container."
                ),
                html.P(
                    dbc.Button("Learn more", color="primary"), className="lead"
                ),
            ],
            fluid=True,
            className="py-3",
        ),
        className="p-3 bg-light rounded-3",
    )


if __name__=='__main__':
    app.run_server(debug=True, port=3000)

    
# https://youtu.be/ln8dyS2y4Nc