import pandas as pd
import numpy as np

df = pd.read_csv(
    'bd.csv',
    sep=';',                  
    engine='python',          
    encoding='utf-8'          
)

dados = df

print("Informações do Gerais:")
print(dados.info())
print("Primeiras 5 linhas:")
print(dados.head())
print("Últimas 5 linhas:")
print(dados.tail())
dados_copia = dados.copy()
dados_copia['Calories'] = pd.to_numeric(dados_copia['Calories'], errors='coerce')  # garantir que seja numérico
dados_copia['Calories'].fillna(0, inplace=True)
print("Coluna 'Calories' após preenchimento dos valores nulos com 0:")
print(dados_copia[['ID', 'Calories']])
dados_copia['Date'] = pd.to_datetime(dados_copia['Date'], errors='coerce')  # ✅ Melhor
dados_copia['Date'].fillna('1900/01/01', inplace=True)
print("Coluna 'Date' após substituição de nulos por '1900/01/01':")
print(dados_copia[['ID', 'Date']])
try:
    dados_copia['Date'] = pd.to_datetime(dados_copia['Date'], format='%Y/%m/%d')
except Exception as e:
    print("Erro na conversão para datetime:", e)
dados_copia['Date'].replace('1900/01/01', np.nan, inplace=True)
dados_copia['Date'] = pd.to_datetime(dados_copia['Date'], errors='coerce')
print("Coluna 'Date' após conversão para datetime (com erros tratados):")
print(dados_copia[['ID', 'Date']])
dados_copia['Date'] = dados_copia['Date'].replace(
    '20201226',
    pd.to_datetime('2020-12-26', format='%Y-%m-%d')
)
dados_copia['Date'] = pd.to_datetime(dados_copia['Date'], errors='coerce')
print("Coluna 'Date' após todas as transformações:")
print(dados_copia[['ID', 'Date']])
dados_copia.dropna(inplace=True)
print("DataFrame final após todas as transformações:")
print(dados_copia)
