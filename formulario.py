from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

app = Dash(__name__)

app.layout = html.Div([
    #Input Idade
    dcc.Input(id='idade', type='number', value=0),
    #botao de submeter
    html.Button('Enviar', id='botao_enviar', n_clicks =0),
    #Output Idade em meses
    html.Div(id='output-meses'),
])

@app.callback(
        output=Output('output-meses', 'children'),
        inputs=Input('botao_enviar', 'n_clicks'),
        state=State('idade', 'value'),
        prevent_initial_call=True
)    
def calcula_meses(n_clicks,idade):
    if n_clicks == 0 or idade is None:
        return ''
    
    return f'Meses: {idade * 12}'

app.run(debug=True)