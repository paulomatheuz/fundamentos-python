"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
    num = int(input("Digite um numero inteiro: "))

    if num % 2 == 0:
        print("O numero {num} é par.")
    else:
        print("O numero {num} é impar.")

except ValueError:
    print("Você não digitou um numero inteiro válido!")