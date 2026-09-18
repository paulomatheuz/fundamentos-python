notas = []
media_aritmetica = 0
maior = 0
menor = 10

for i in range(5):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)
    media_aritmetica += nota

    if 0 < nota > 10:
        print("Nota inválida!")
        break

    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota
        
print(notas)
print(f"Media aritmetica das notas {media_aritmetica / 5}")
print(f"Menor: {menor}")
print(f"Maior: {maior}")