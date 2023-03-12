from classes import Reclamacoes, Elogios

reclamacoes = Reclamacoes()
elogios = Elogios()

print("Bem-vindo ao sistema de Ouvidoria!")

while True:
    print("-*-" * 10)
    print()
    print("1 - Adicionar Reclamações.")
    print("2 - Adicionar Elogios.")
    print("3 - Listar Reclamações e Elogios")
    print("4 - Excluir Reclamações e Elogios")
    print("5 - Editar Reclamações e Elogios")
    print("6 - SAIR!")
    print()
    print("-*-" * 10)

    opcao = int(input("Digite sua opção: "))
    if opcao == 1:
        print("Adicionar reclamações")
        reclamacao = input("Faça sua reclamação: ")
        reclamacoes.addReclamacoes(reclamacao)

    elif opcao == 2:
        print("Adicionar elogios")
        elogio = input("Faça seu elogio: ")
        elogios.addElogios(elogio)

    elif opcao == 3:
        print("Listar Reclamações e Elogios")
        print("Reclamações:")
        reclamacoes.getReclamacoes()
        print("Elogios:")
        elogios.getElogios()
    
    elif opcao == 4:
        print("0 - Reclamação")
        print("1 - Elogio")
        excluir = int(input("Excluir Reclamação ou Elogio? "))
        if excluir == 0:
            reclamacoes.deleteReclamacoes()
        elif excluir == 1:
            elogios.deleteElogios()
    
    elif opcao == 5:
        print("0 - Reclamação")
        print("1 - Elogio")
        editar = int(input("Editar Reclamação ou Elogio? "))
        if editar == 0:
            reclamacoes.setReclamacoes()
        elif editar == 1:
            elogios.setElogios()
    
    elif opcao == 6:
        print("Obrigado por usar nossa Ouvidoria")
        break
