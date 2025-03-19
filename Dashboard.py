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
app.layout = [
    html.Div(children='My First App with Data and a Graph'),
    dcc.Dropdown(opcoes, id='dropdown'),
    dcc.Graph(figure=fig, id='grafico')
]

@app.callback(
    Output('grafico', 'figure'),
    Input('dropdown', 'value'),

)

def update_output(value):
        if value == 'Todas criptomoedas':
            fig = px.histogram(df, x='id', y='preços', color='id', barmode='group')
        else:
            df_filtrado = df.loc[df['nome'] == value]
            fig = px.histogram(df_filtrado, x='id', y='preços', color='id', barmode='group')
            print(df_filtrado)
        return fig


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
