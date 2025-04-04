from ucimlrepo import fetch_ucirepo
from dash import dcc, html
import plotly.express as px
import dash_bootstrap_components as dbc

heart_disease = fetch_ucirepo(id=45)
dados = heart_disease.data.features

dados['doenca'] = (heart_disease.data.targets > 0) * 1

# Plot do gráfico 
figura_histograma = px.histogram(dados, x='age')

# Boxlot do ploty das idades por doença, colorido por doença
figura_boxplot = px.box(dados, x='doenca', y='age', color='doenca')

#Divs para os gráficos
div_histograma = html.Div([
        html.H4("Histograma de Idades", className="text-center"),
        dcc.Graph(figure=figura_histograma),
        ])

div_boxplot = html.Div([
        html.H4("Boxplot de Idades por Doença Cardíaca",className="text-center"),
        dcc.Graph(figure=figura_boxplot),
        ])

layout = html.Div([
    html.H1("Análise de Dados de Doença Cardíaca", className="text-center"),
    dbc.Container([
        dbc.Row([
            dbc.Col(div_histograma, width=6),
            dbc.Col(div_boxplot, width=6)
        ]),
    ])
 
])