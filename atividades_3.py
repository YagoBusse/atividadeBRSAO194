"""1- Área da circunferência

A fórmula para calcular a área de uma circunferência é: área = π ×raio2. Considerando para
este problema que π = 3.14159265: 

• Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π. 

Entrada: A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável
raio.
Saída: Apresente a mensagem "A=" seguido pelo valor da variável area, conforme exemplo
abaixo, com 4 casas após o ponto decimal."""

print("1------------------\n")
raio = float(input("Digite o valor do raio: "))
pi = 3.14159265
area = pi * (raio ** 2)
print("A = {:.4f}".format(area))

"""2- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

Criança (0-12 anos),

Adolescente (13-17 anos),

Adulto (18-59 anos)

Idoso (60 anos ou mais)."""

print("\n2------------------\n")
idade = int(input("Digite sua idade: "))
if idade >= 0 and idade <= 12:
    print("Classificação: Criança")
elif idade >= 13 and idade <= 17:
    print("Classificação: Adolescente")
elif idade >= 18 and idade <= 59:
    print("Classificação: Adulto")
else:
    print("Classificação: Idoso")


"""3- Calculadora de IMC


Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.


< 18.5: classificacao = "Abaixo do peso" 

< 25: classificacao = "Peso normal"

 < 30: classificacao = "Sobrepeso"

 Para os demais cenários: classificacao = "Obeso"""
print("\n3------------------\n")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"
print("IMC: {:.2f}".format(imc))
print("Classificação: {}".format(classificacao))

"""4- Conversor de Temperatura 

Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter."""

print("\n4------------------\n")
temp = float(input("Digite a temperatura: "))
unidade_origem = input("Digite a unidade de origem (C/F/K): ").upper()
unidade_destino = input("Digite a unidade de destino (C/F/K): ").upper()

if unidade_origem == "C":
    if unidade_destino == "F":
        temp_convertida = (temp * 9/5) + 32
    elif unidade_destino == "K":
        temp_convertida = temp + 273.15
    else:
        temp_convertida = temp
elif unidade_origem == "F":
    if unidade_destino == "C":
        temp_convertida = (temp - 32) * 5/9
    elif unidade_destino == "K":
        temp_convertida = (temp - 32) * 5/9 + 273.15
    else:
        temp_convertida = temp
elif unidade_origem == "K":
    if unidade_destino == "C":
        temp_convertida = temp - 273.15
    elif unidade_destino == "F":
        temp_convertida = (temp - 273.15) * 9/5 + 32
    else:
        temp_convertida = temp
else:
    print("Unidade de origem inválida.")

print("Temperatura convertida: {:.2f} {}".format(temp_convertida, unidade_destino))

"""5- Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.

Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400."""
print("\n5------------------\n")
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O ano {} é bissexto.".format(ano))
else:
    print("O ano {} não é bissexto.".format(ano))

"""6- Calculadora de Comissão


Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas
efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais. 

Entrada: O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de
dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e
montante total das vendas efetuadas por este vendedor, respectivamente. 

Saída: Imprima o total que o funcionário deverá receber, conforme exemplo fornecido."""

print("\n6------------------\n")
nome_vendedor = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: "))
total_vendas = float(input("Digite o total de vendas efetuadas: "))
comissao = total_vendas * 0.15
salario_total = salario_fixo + comissao
print("O total a receber é: R$ {:.2f}".format(salario_total))

"""7- Calculadora da Média

Faça um programa que leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". 

Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".

No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno. Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2). e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais) ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). 

Para estes dois casos
(aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem "Media
final: " seguido da média final para esse aluno.


Entrada: A entrada contém quatro números de ponto flutuante correspondentes às notas dos alunos.


Saída: Todas as respostas devem ser apresentadas com uma casa decimal. As mensagens devem ser impressas conforme a descrição do problema. Não esqueça de imprimir o enter após o final de cada linha, caso contrário obterá "Presentation Error"."""

print("\n7------------------\n")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 * 2 + nota2 * 3 + nota3 * 4 + nota4 * 1) / 10
print("Media: {:.1f}".format(media))