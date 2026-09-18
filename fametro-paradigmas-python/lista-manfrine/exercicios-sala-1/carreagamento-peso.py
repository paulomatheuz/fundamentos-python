peso_pacote = 0
peso_pacote_total = 0

while peso_pacote_total < 20:
    peso_pacote = float(input("Digite o peso de mais um pacote: "))
    peso_pacote_total += peso_pacote

    if peso_pacote_total > 20:
        print(f"Peso acima do limite!")
        break
    
    print(f"Peso total: {peso_pacote_total}")