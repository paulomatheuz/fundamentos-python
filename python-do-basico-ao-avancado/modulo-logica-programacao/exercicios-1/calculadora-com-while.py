"""
Faça uma calculadora com while.
"""

while True:
    numero1 = input("Digite o primeiro numero: ")
    numero2 = input("Digite o segundo numero: ")
    operador = input("Digite um operador matematico (+ - / *): ")

    numeros_validos = None

    try:
        num1_float = float(numero1)
        num2_float = float(numero2)
        numeros_validos = True
    except ValueError:
        numeros_validos = None

    if numeros_validos is None:
        print("Numeros invalidos!")
        continue

    operadores_permitidos = "+-/*"

    if operador not in operadores_permitidos:
        print("Operador não permitido")
        continue

    if len(operador) > 1:
        print("Somente um operador por vez!")
        continue

    if operador == "+":
        resultado = num1_float + num2_float
    elif operador == "-":
        resultado = num1_float - num2_float
    elif operador == "*":
        resultado = num1_float * num2_float
    else:
        if num2_float == 0:
            print("Divisão por zero!")
            continue
        else:
            resultado = num1_float / num2_float

    print(f"Resultado: {resultado}")

    sair = input("Quer sair? [S]: ").lower().startswith("s")

    if sair is True:
        break