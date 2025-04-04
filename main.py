from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pages
from app import app

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Gráficos", href="/graficos")),
        dbc.NavItem(dbc.NavLink("Formulário", href="/formulario")),
        
    ],
    brand="Dashboard de Doença Cardíaca",
    brand_href="/",
    color="primary",
    dark=True,
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content'),
])

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)

def show_page(pathname):
    if pathname == '/graficos':
        return pages.graph.layout
    
    elif pathname == '/formulario':
        return pages.forms.layout
    else:
        return html.P('404: Not found')

app.run(debug=True)