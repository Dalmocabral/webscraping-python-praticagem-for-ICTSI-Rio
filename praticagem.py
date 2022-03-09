import pandas as pd
import json

def raspagem():
     df = pd.read_html('http://www.praticagem-rj.com.br/', match=f'TECONT{i}')
     tabela = df[3]
        
        

    filter_praticagem = ['POB', 'NAVIO', 'CALADO', 'MANOBRA', 'DE', 'PARA' ]

    new_tabela = tabela.filter(items=filter_praticagem)

    x = new_tabela.to_json(orient='records')

    data = json.loads(x)

    return data
