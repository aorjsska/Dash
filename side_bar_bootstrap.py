from dash import Dash, dcc, html, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Bootstrap/Side-Bar/iranian_students.csv')

app = Dash(__name__)
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
# app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

sidebar = dbc.Card([
    dbc.CardBody([
        html.H2("Dashboard", className="display-6"),
        html.Hr(),
        html.P(
            "Number of students per education level", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Static Test", href="/statictest", active="exact"),
                dbc.NavLink("Unit Test", href="/unittest", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ])
])

content = html.Div(id="page-content")

app.layout = dbc.Container([
    dcc.Location(id="url"),
    dbc.Row([
        dbc.Col(sidebar,width=2),
        dbc.Col(content)
    ])
], fluid=True)

home_layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Home page")
        ]
        )
    ]
    )
], fluid=True)

statictest_layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Tabs([
                dbc.Tab(id="tab-hdp", tab_id="tab-hdp", label="hdp", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
                dbc.Tab(id="tab-lv4", tab_id="tab-lv4", label="lv4", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
                dbc.Tab(id="tab-others", tab_id="tab-others", label="others", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
            ], id="tabs", active_tab="tab-hdp")
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.Div(id="tab_div", children=[])
        ])
    ])
], fluid=True)

unittest_layout = html.Div(id="unit-test", children="unit test page")

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [
            home_layout
                # html.H1('Kindergarten in Iran',
                #         style={'textAlign':'center'}),
                # dcc.Graph(id='bargraph',
                #          figure=px.bar(df, barmode='group', x='Years',
                #          y=['Girls Kindergarten', 'Boys Kindergarten']))
                ]
    elif pathname == "/statictest":
        return [
            statictest_layout
                # html.H1('Grad School in Iran',
                #         style={'textAlign':'center'}),
                # dcc.Graph(id='bargraph',
                #          figure=px.bar(df, barmode='group', x='Years',
                #          y=['Girls Grade School', 'Boys Grade School']))
                ]
    elif pathname == "/unittest":
        return [
            unittest_layout
                # html.H1('High School in Iran',
                #         style={'textAlign':'center'}),
                # dcc.Graph(id='bargraph',
                #          figure=px.bar(df, barmode='group', x='Years',
                #          y=['Girls High School', 'Boys High School']))
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

@app.callback(
    Output(component_id="tab_div", component_property="children"),
    [Input(component_id="tabs", component_property="active_tab")]
)
def switch_tab(tab_chosen):
    return [
        html.Br(),
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    dbc.Tabs([
                        dbc.Tab(tab_id="tab-10th", label="10th", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
                        dbc.Tab(tab_id="tab-9th", label="9th", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
                        dbc.Tab(tab_id="tab-8th", label="8th", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
                        dbc.Tab(tab_id="tab-7th", label="7th", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
                        dbc.Tab(tab_id="tab-6th", label="6th", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
                        dbc.Tab(tab_id="tab-5th", label="5th", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger"),
                    ], id="tabs2", active_tab="tab-10th")
                ])
            ])
        ], fluid=True)
    ]



if __name__=='__main__':
    app.run_server(debug=True, port=3000)

    
# https://youtu.be/ln8dyS2y4Nc