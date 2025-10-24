import os
import json
from random import random
from datetime import datetime
import time


import requests
import pandas as pd
# import seaborn as sns

URL = 'https://www2.cetip.com.br/ConsultarTaxaDi/ConsultarTaxaDICetip.aspx'

# # Capturando data e hora
# # hoje = pd.Timestamp.now()]
# hoje = datetime.now()

# # Brincando com as datas
# data = hoje.strftime('%d/%m/%Y')
# data_escrita = hoje.strftime('%A, %B de %Y')

# # Brincando com as horas
# hora = hoje.strftime('%H:%M:%S')
# hora_AM_PM = hoje.strftime('%p %I:%M')

for _ in range(0, 10):
    data_de_hoje = datetime.now()
    data = data_de_hoje.strftime('%Y/%m/%d')
    hora = data_de_hoje.strftime('%H:%M:%S')

    try:
        resposta = requests.get(URL)
        resposta.raise_for_status()
    except requests.HTTPError as exc:
        print('A pagina parece estar fora do ar.')
        cdi = None
    except Exception as exc:
        print('Erro, parando a execução.')
        raise exc
    else:
        dado = json.loads(resposta.text)
        cdi = float(dado['taxa'].replace(',','.')) + (random() - 0.5)
    
    if os.path.exists('C:/Users/lord_/.vscode/codes/Arquivo/taxa-cdi.csv') == False:
        with open(file='C:/Users/lord_/.vscode/codes/Arquivo/taxa-cdi.csv', mode="w", encoding='utf8') as fp:
            fp.write('data,hora,taxa\n')
    
    with open(file='C:/Users/lord_/.vscode/codes/Arquivo/taxa-cdi.csv', mode='a', encoding='utf8') as fp:
        fp.write(f'{data},{hora},{cdi}\n')
    
    time.sleep(2 + (random() - 0.5))
        

# df = pd.read_csv('C:/Users/lord_/.vscode/codes/Arquivo/dados/taxa-cdi.csv')

# # print(df['data'])
# for x in ['taxa']:
#     print(df[x])