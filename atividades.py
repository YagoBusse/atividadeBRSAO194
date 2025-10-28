import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
#Atividade Prática 01
#1- Programa de Saudação
print("1------------------")
print("Hello, World!")

#2- Calculadora de Soma

num1 = 12
num2 = 14

soma = num1 + num2

print("2------------------")
print("A soma é:", soma)
#3- Calculadora de Volume

largura = 12
altura = 14
profundidade = 20

volume = largura * altura * profundidade
print("3------------------")
print("O volume é:", volume, "cm³")


#4- Calculadora de Preço Total
nome_produto = "Cadeira Infantil"
preco_unitario = 12.40  
quantidade = 3

preco_total = preco_unitario * quantidade
print("4------------------")
print(locale.format_string("O preço total é: R$ %.2f", preco_total))

#5- Calculadora de Número Inteiro
print("5------------------")
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

DIFERENCA = (A * B) - (C * D)

print("DIFERENCA =", DIFERENCA)

