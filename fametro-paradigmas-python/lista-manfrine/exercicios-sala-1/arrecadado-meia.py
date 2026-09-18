qtd_pessoas = int(input("Digite a quantidade de pessoas: "))

total_arrecadado = 0
pessoa_pagou_meia = 0

for i in range(qtd_pessoas):
    idade_pessoa = int(input("DIgite a sua idade: "))
    if 18 < idade_pessoa < 60:
        total_arrecadado += 30
    else:
        total_arrecadado += 15
        pessoa_pagou_meia += 1

print(f"Total arrecadado: {total_arrecadado}")
print(f"Quantidade de pessoas que pagaram meia: {pessoa_pagou_meia}")