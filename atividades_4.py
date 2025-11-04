"""Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. 
A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:

A calculadora deve solicitar ao usuário que insira dois números e uma operação.

As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).

O programa deve continuar solicitando entradas até que uma operação válida seja concluída.

Trate os seguintes erros:

Entrada inválida (não numérica) para os números

Divisão por zero

Operação inválida



Use try/except para capturar e tratar os erros apropriadamente.

Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.

Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa."""

from builtins import Exception, ValueError, ZeroDivisionError, any, float, input, len, print, sum


while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError("Divisão por zero não é permitida.")
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida. Use apenas +, -, * ou /.")

        print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
        break

    except ValueError as ve:
        print(f"Erro de valor: {ve}. Por favor, tente novamente.")
    except ZeroDivisionError as zde:
        print(f"Erro de divisão: {zde}. Por favor, tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente.")

print("2------------------\n")

"""Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve continuar solicitando notas até que o professor digite 'fim'. 
Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma."""

notas = []
while True:
    entrada = input("Digite a nota (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite uma nota de 0 a 10.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

if notas:
    media = sum(notas) / len(notas)
    print(f"A média da turma é: {media:.2f}")
else:
    print("Nenhuma nota válida foi registrada.")

print("3------------------\n")

"""Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. O programa deve 
continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'."""
while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    if senha.lower() == 'sair':
        print("Encerrando o programa.")
        break
    if len(senha) >= 8 and any(char.isdigit() for char in senha):
        print("Senha forte! Acesso concedido.")
        break
    else:
        print("Senha fraca. Tente novamente.")

print("4------------------\n")

"""Crie um programa que solicite ao usuário que insira números inteiros. O programa deve continuar solicitando números até que o usuário digite 'fim'. Para cada 
número inserido, o programa deve informar se é par ou ímpar. Se o usuário inserir algo que não seja um número inteiro, o programa deve
informar o erro e continuar. No final, o programa deve exibir a quantidade de números pares e ímpares inseridos."""

pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            pares += 1
            print(f"{numero} é par.")
        else:
            impares += 1
            print(f"{numero} é ímpar.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
