"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

try:
    hora = int(input("Digite a hora atual (0-23): "))

    if 0 <= hora < 12:
        print("Bom dia!")
    elif 12 <= hora < 18:
        print("Boa tarde!")
    elif 18 <= hora < 24:
        print("Boa noite!")
    else:
        print("Hora inválida! Digite um valor entre 0 e 23.")

except ValueError:
    print("Por favor, digite apenas números inteiros.")