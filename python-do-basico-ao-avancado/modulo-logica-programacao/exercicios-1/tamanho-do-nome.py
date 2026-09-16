"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

name_user = input("Digite seu primeiro nome: ").strip()

number_letters = len(name_user)

if number_letters <= 4:
    print("Seu nome é curto!")
elif number_letters <= 6:
    print("Seu nome é normal!")
else:
    print("Seu nome é muito grande!")