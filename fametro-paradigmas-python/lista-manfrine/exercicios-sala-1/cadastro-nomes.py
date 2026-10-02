import os

nomes = []

while True:
    print("\n1 - Cadastrar nome")
    print("2 - Mostrar os nomes")
    print("3 - Buscar um nome")
    print("4 - Alterar um nome")
    print("5 - Excluir um nome")
    print("6 - Excluir todos os nomes")
    print("0 - Sair")

    opcao = input("Digite a opção escolhida: ")
    os.system("cls")

    if opcao == "1":
        nome = input("Nome: ")
        nomes.append(nome)
        print("Nome cadastrado!")

    elif opcao == "2":
        if not nomes:
            print("Nada a listar!")
        else:
            for indice, nome in enumerate(nomes):
                print(f"{indice + 1} - {nome}")

    elif opcao == "3":
        nome = input("Digite o nome para buscar: ")
        if nome in nomes:
            print(f"Nome encontrado na posição {nomes.index(nome) + 1}.")
        else:
            print("Nome não encontrado!")

    elif opcao == "4":
        nome = input("Qual nome você quer alterar? ")
        if nome in nomes:
            indice = nomes.index(nome)
            nomes[indice] = input("Digite o novo nome: ")
            print("Nome alterado!")
        else:
            print("Nome não encontrado!")

    elif opcao == "5":
        nome = input("Qual nome você quer apagar? ")
        if nome in nomes:
            nomes.remove(nome)
            print("Nome excluído!")
        else:
            print("Nome não encontrado!")

    elif opcao == "6":
        nomes.clear()
        print("Todos os nomes foram excluídos!")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")
