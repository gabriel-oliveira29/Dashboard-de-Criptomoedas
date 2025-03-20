# Import packages
from dash import Dash, html, dcc, Input,Output
import pandas as pd
import plotly.express as px
from TratamentoDeDados import df

# Initialize the app
app = Dash()

opcoes = list(df['nome'].unique())
opcoes.append('Todas criptomoedas')

fig = px.histogram(df, x='id', y='preços', color='id')

# App layout
app.layout = html.Div ([
    html.H1(children='Criptomoedas'),
    dcc.Dropdown(opcoes, value='Todas criptomoedas' , id='dropdown', multi=True),
    dcc.Graph(figure=fig, id='grafico')
])

@app.callback(
    Output('grafico', 'figure'),
    Input('dropdown', 'value')

)

def update_output(value):
    if isinstance(value, str):
        value = [value]

    if 'Todas criptomoedas' in value or not value:  
        fig = px.histogram(df, x='id', y='preços', color='id')
        
    else:
        df_filtrada = df[df['nome'].isin(value)]
        fig = px.histogram(df_filtrada, x='id', y='preços', color='id')

    fig.update_layout(yaxis_type="log")
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
                