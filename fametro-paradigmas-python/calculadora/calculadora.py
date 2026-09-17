def calculadora():
    while True:
        print("\n--- CALCULADORA ---")
        
        entrada = input("Digite o primeiro número (ou 's' para sair): ").strip()
        if entrada.lower() == 's':
            print("Encerrando a calculadora. Até logo!")
            break

        try:
            valor1 = float(entrada)
            operacao = input("Digite a operação (+, -, *, /): ").strip()
            valor2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: Por favor, digite apenas valores numéricos válidos.")
            continue

        match operacao:
            case "+":
                resultado = valor1 + valor2
            case "-":
                resultado = valor1 - valor2
            case "*":
                resultado = valor1 * valor2
            case "/":
                if valor2 == 0:
                    print("Erro: Divisão por zero não é permitida.")
                    continue
                resultado = valor1 / valor2
            case _:
                print("Erro: Operação inválida.")
                continue

        print(f"\nResultado: {valor1} {operacao} {valor2} = {resultado}")

if __name__ == "__main__":
    calculadora()
