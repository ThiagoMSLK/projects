# Bibliotecas nativas
import os
import time
import json
import csv
from sys import argv
from random import random
from datetime import datetime

# Bibliotecas externas
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Variavel fixa
URL = 'https://www2.cetip.com.br/ConsultarTaxaDi/ConsultarTaxaDICetip.aspx'

# Loop para gerar dados artificiais
    # Armazenando as variaveis data e hora
for _ in range (0,10):
    data_e_hora = pd.Timestamp.now()
    # data_e_hora = datetime.now()
    data = datetime.strftime(data_e_hora, '%Y/%m/%d')
    hora = datetime.strftime(data_e_hora, '%H:%M:%S')

    # Captando a taxa CDI do site da B3
    try:
        response = requests.get(URL)
        response.raise_for_status()
    except requests.HTTPError as exc:
        print('Dados não encontrados, continuando')
        cdi = None
    except Exception as exs:
        print('Erro, parando a execução')
        raise exc
    else:
        dado = json.loads(response.text)
        cdi = float(dado['taxa'].replace(',','.')) + (random() - 0.5)
    
    # Verificando se o arquivo "taxa-cdi.csv" existe
    if os.path.exists('C:/Users/lord_/.vscode/codes/Arquivo/taxa-cdi.csv') == False:
        with open(file='C:/Users/lord_/.vscode/codes/Arquivo/taxa-cdi.csv', mode= 'w', encoding='utf8') as fp:
            fp.write('data,hora,taxa\n')
    # Salvando dados no arquivo "taxa-cdi.csv"
    with open(file='C:/Users/lord_/.vscode/codes/Arquivo/taxa-cdi.csv', mode='a', encoding='utf8') as fp:
        fp.write(f'{data},{hora},{cdi}\n')

    # Gerando variações artificiais
    time.sleep(2 + (random() - 0.5))

# Extraindo as colunas de hora e taxa
df = pd.read_csv('C:/Users/lord_/.vscode/codes/Arquivo/taxa-cdi.csv')

# Salvando no grafico
grafico = sns.lineplot(x=df['hora'], y=df['taxa'])
_ = grafico.set_xticklabels(labels=df['hora'], rotation= 90)
grafico.get_figure().savefig(f'{argv[1]}.png')
# grafico.get_figure().savefig(f'teste{hora}.png')

plt.show()