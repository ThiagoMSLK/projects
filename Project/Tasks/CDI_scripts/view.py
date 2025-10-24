import csv
from sys import argv
import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns

# Extraindo coluna hora e taxa

df = pd.read_csv('C:/Users/lord_/.vscode/codes/Arquivo/taxa-cdi.csv')

# Salvando no grafico

grafico = sns.lineplot(x=df['hora'], y=df['taxa'])
_ = grafico.set_xticklabels(labels=df['hora'], rotation=90)
# grafico.get_figure().savefig(f'{argv[1]}.png')
nome = input('Escolha um nome: ')
grafico.get_figure().savefig(f'C:/Users/lord_/.vscode/codes/Arquivo/{nome}.png')

plt.show()