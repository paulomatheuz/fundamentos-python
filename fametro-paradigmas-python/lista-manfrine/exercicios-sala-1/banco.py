saldo_total = 0.0

def saldo():
    global saldo_total
    print(f"\nSaldo: {saldo_total}")
    
def depositar(x):
    global saldo_total
    saldo_total += x

def sacar(y):
    global saldo_total
    saldo_total -= y

while True:
    print("\n### CENTRAL BANK ###")
    print("1 - VER SALDO")
    print("2 - DEPOSITAR")
    print("3 - SACAR")
    print("4 - SAIR DO BANCO")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        saldo()      
    elif opcao == "2":
        print("FUNÇÃO DEPOSITAR: ")
        x = float(input("Digite o valor do deposito: "))
        depositar(x)
        print(f"\nSaldo atual apos deposito: {saldo_total}")
    elif opcao == "3":
        print("FUNCAO SACAR")
        y = float(input("Digite o valor do saque: "))
        sacar(y)
        print(f"\nSaldo atual apos saque: {saldo_total}")
    elif opcao == "4":
        break