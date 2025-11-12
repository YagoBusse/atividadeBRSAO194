# Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning. Calcule a média e o desvio padrão do tempo de exercução constantes nesses logs e plote um gráfico mostrando os tempos de execução para cada modelo treinado.

import re
import statistics
import matplotlib.pyplot as plt
import numpy as np
import requests
import os
from datetime import datetime
import json
import pandas as pd
# Função para ler o arquivo de log e extrair os tempos de execução
def ler_log_e_extrair_tempos(caminho_arquivo):
    tempos = []
    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            match = re.search(r'Tempo de execução: (\d+\.\d+) segundos', linha)
            if match:
                tempos.append(float(match.group(1)))
    return tempos
# Função para calcular a média e o desvio padrão
def calcular_estatisticas(tempos):
    media = statistics.mean(tempos)
    desvio_padrao = statistics.stdev(tempos)
    return media, desvio_padrao
# Função para plotar os tempos de execução
def plotar_tempos(tempos):
    plt.figure(figsize=(10, 5))
    plt.plot(tempos, marker='o')
    plt.title('Tempos de Execução dos Modelos de Machine Learning')
    plt.xlabel('Execução')
    plt.ylabel('Tempo (segundos)')
    plt.grid(True)
    plt.show()
# Caminho do arquivo de log
caminho_arquivo_log = 'log_treinamento.txt'
# Extrair tempos do arquivo de log
tempos_execucao = ler_log_e_extrair_tempos(caminho_arquivo_log)
# Calcular estatísticas
media, desvio_padrao = calcular_estatisticas(tempos_execucao)
print(f'Média dos tempos de execução: {media:.2f} segundos')
print(f'Desvio padrão dos tempos de execução: {desvio_padrao:.2f} segundos')
# Plotar os tempos de execução
plotar_tempos(tempos_execucao)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~')

# Programa em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações pessoais, como Nome, Idade e Cidade.

import csv
# Dados para escrever no arquivo CSV
dados_pessoais = [
    ['Nome', 'Idade', 'Cidade'],
    ['Alice', 30, 'São Paulo'],
    ['Bruno', 25, 'Rio de Janeiro'],
    ['Carla', 28, 'Belo Horizonte'],
    ['Daniel', 35, 'Curitiba']
]
# Caminho do arquivo CSV
caminho_arquivo_csv = 'dados_pessoais.csv'
# Escrever os dados no arquivo CSV
with open(caminho_arquivo_csv, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerows(dados_pessoais)
print(f'Dados pessoais escritos no arquivo {caminho_arquivo_csv}')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~')

# Programa em Python que leia dados de um arquivo CSV contendo informações pessoais, como Nome, Idade e Cidade, e exiba esses dados no console.

import csv
# Caminho do arquivo CSV
caminho_arquivo_csv = 'dados_pessoais.csv'
# Ler e exibir os dados do arquivo CSV
with open(caminho_arquivo_csv, 'r', encoding='utf-8') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        print(f'Nome: {linha[0]}, Idade: {linha[1]}, Cidade: {linha[2]}')
print(f'Dados pessoais lidos do arquivo {caminho_arquivo_csv}')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~')

# Programa em Python que escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, como Nome, Idade e Cidade.

import json
# Dados para escrever no arquivo JSON
dados_pessoa = {
    'nome': 'Alice',
    'idade': 30,
    'cidade': 'São Paulo'
}
# Caminho do arquivo JSON
caminho_arquivo_json = 'dados_pessoa.json'
# Escrever os dados no arquivo JSON
with open(caminho_arquivo_json, 'w', encoding='utf-8') as arquivo_json:
    json.dump(dados_pessoa, arquivo_json, ensure_ascii=False, indent=4)
print(f'Dados da pessoa escritos no arquivo {caminho_arquivo_json}')    
# Ler e exibir os dados do arquivo JSON
with open(caminho_arquivo_json, 'r', encoding='utf-8') as arquivo_json:
    dados_lidos = json.load(arquivo_json)
    print(f'Nome: {dados_lidos["nome"]}, Idade: {dados_lidos["idade"]}, Cidade: {dados_lidos["cidade"]}')
print(f'Dados da pessoa lidos do arquivo {caminho_arquivo_json}')

print('~~~~~~~~~~~~~~~~~~~~~~~~~~')