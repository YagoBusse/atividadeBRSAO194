# Programa que gera uma senha aleatória com o tamanho especificado pelo usuário.
import random
import string
tamanho = int(input("Digite o tamanho da senha desejada: "))
caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ''.join(random.choice(caracteres) for i in range(tamanho))
print("Senha gerada:", senha)

print('~~~~~~~~~~~~~~~~~~~~~~~~')

# Programa que consome a API Random User e exibe o nome, email e país de um usuário aleatório.

import requests
response = requests.get("https://randomuser.me/api/")
data = response.json()
usuario = data['results'][0]
nome = f"{usuario['name']['first']} {usuario['name']['last']}"
email = usuario['email']
pais = usuario['location']['country']
print(f"Nome: {nome}\nEmail: {email}\nPaís: {pais}")

print('~~~~~~~~~~~~~~~~~~~~~~~~')

# Programa que consulta o endereço completo a partir de um CEP utilizando a API ViaCEP. O usuário deve informar o CEP e o programa deve exibir o logradouro, bairro, cidade e estado correspondentes.

import requests
cep = input("Digite o CEP (somente números): ")
response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
data = response.json()
if 'erro' not in data:
    logradouro = data['logradouro']
    bairro = data['bairro']
    cidade = data['localidade']
    estado = data['uf']
    print(f"Logradouro: {logradouro}\nBairro: {bairro}\nCidade: {cidade}\nEstado: {estado}")
else:
    print("CEP não encontrado.")

print('~~~~~~~~~~~~~~~~~~~~~~~~')

# Programa que consulta a cotação atual de uma moeda em relação ao Real Brasileiro (BRL) utilizando a API AwesomeAPI. O usuário deve informar o código da moeda (ex: USD, EUR) e o programa deve exibir o valor atual, valor máximo e valor mínimo da moeda em BRL.

import requests
moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
response = requests.get(f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL")
data = response.json()
if f"{moeda}BRL" in data:
    cotacao = data[f"{moeda}BRL"]
    valor_atual = cotacao['bid']
    valor_maximo = cotacao['high']
    valor_minimo = cotacao['low']
    data_hora = cotacao['create_date']
    print(f"Cotação de {moeda} em BRL:\nValor Atual: R$ {valor_atual}\nValor Máximo: R$ {valor_maximo}\nValor Mínimo: R$ {valor_minimo}\nÚltima Atualização: {data_hora}")
else:
    print("Moeda não encontrada.")

print('~~~~~~~~~~~~~~~~~~~~~~~~')