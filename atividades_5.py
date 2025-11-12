# Função para calcular a gorjeta com base no valor da conta e na porcentagem desejada

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta
# Exemplo de uso
valor_conta = 300.0  # valor da conta em reais
porcentagem_gorjeta = 15  # porcentagem da gorjeta
valor_gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
print(f'Valor da gorjeta: R$ {valor_gorjeta:.2f}')

# Saída esperada: Valor da gorjeta: R$ 15.00
print('~~~~~~~~~~~~~~~~~~~~~~~~')

#Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.

import string
def eh_palindromo(texto):
    # Remover espaços e pontuação, e converter para minúsculas
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    # Verificar se o texto limpo é igual ao seu reverso
    return texto_limpo == texto_limpo[::-1]
# Exemplo de uso
frase = "A man, a plan, a canal: Panama"
if eh_palindromo(frase):
    print("Sim")
else:
    print("Não")
# Saída esperada: Sim
print('~~~~~~~~~~~~~~~~~~~~~~~~')

# Crie uma função que calcule o preço final de um produto após aplicar um desconto percentual.

def calcular_preco_final(preco_original, percentual_desconto):
    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto
    return preco_final
# Exemplo de uso
preco_original = 250.75  # preço do produto em reais
percentual_desconto = 10  # percentual de desconto
preco_final = calcular_preco_final(preco_original, percentual_desconto)
print(f'Preço final após desconto: R$ {preco_final:.2f}')
# Saída esperada: Preço final após desconto: R$ 225.68

print('~~~~~~~~~~~~~~~~~~~~~~~~')

# Função que receba o ano de nascimento de uma pessoa e o ano atual, e retorne a idade dessa pessoa em dias.

def calcular_idade_em_dias(ano_nascimento, ano_atual):
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # Considerando anos não bissextos
    return idade_dias
# Exemplo de uso
ano_nascimento = 1990
ano_atual = 2024
idade_dias = calcular_idade_em_dias(ano_nascimento, ano_atual)
print(f'Idade em dias: {idade_dias} dias')

# Saída esperada: Idade em dias: 12410 dias

print('~~~~~~~~~~~~~~~~~~~~~~~~')