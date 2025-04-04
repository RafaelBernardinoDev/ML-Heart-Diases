from ucimlrepo import fetch_ucirepo
import plotly.express as px
from dash import Dash, dcc, html

heart_disease = fetch_ucirepo(id=45)
dados = heart_disease.data.features

dados['doenca'] = (heart_disease.data.targets > 0) * 1

# Plot do gráfico 
figura_histograma = px.histogram(dados, x='age', title='Histograma de idades')

# Boxlot do ploty das idades por doença, colorido por doença
figura_boxplot = px.box(dados, x='doenca', y='age', color='doenca', title='Boxplot de idades por doença cardíaca')

#Divs para os gráficos
div_histograma = html.Div([
        html.H2("Histograma de Idades"),
        dcc.Graph(figure=figura_histograma),
        ])

div_boxplot = html.Div([
        html.H2("Boxplot de Idades por Doença Cardíaca"),
        dcc.Graph(figure=figura_boxplot),
        ])

# Start do app
app = Dash(__name__)
app.layout = html.Div([
    html.H1("Análise de Dados de Doença Cardíaca"),
    div_histograma,
    div_boxplot,
    ])
 
app.run(debug=True)