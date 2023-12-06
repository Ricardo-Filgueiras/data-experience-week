# limpando dados 
# scripty python para tratar dados csv para substituir ';' por ',' nos arquivos csv 



import pandas as pd
import os

def editor(arquivo):
    # Lê o arquivo CSV usando ponto e vírgula como delimitador
    df = pd.read_csv(arquivo, sep=';')

    # Extrai o nome do arquivo e a extensão
    nome_arquivo, extensao = os.path.splitext(arquivo)

    # Define o nome do arquivo de saída com extensão .csv
    arquivo_saida = nome_arquivo + '_modificado.csv'

    # Salva o DataFrame no novo arquivo CSV
    df.to_csv(arquivo_saida, sep=',', index=False)

    # Retorna o DataFrame lido (opcional, dependendo do que você deseja fazer)
    return df

# Exemplo de uso
arquivo00002 = editor('seuarquivo.csv')
