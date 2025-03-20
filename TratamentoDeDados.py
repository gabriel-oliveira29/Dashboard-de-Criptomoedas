from Api import cotacao
import pandas as pd

lista = []

for moeda in cotacao['data']:
    lista.append({
        'nome' : moeda['name'],
        'id' : moeda['symbol'],
        'preços' : moeda['priceUsd']
    })
    
df = pd.DataFrame(lista)
print(cotacao)