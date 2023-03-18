opcao1 = input()
opcao2 = input()
opcao3 = input()

if opcao1 == "vertebrado":
    if opcao2 == "ave":
        if opcao3 == "carnivoro":
            print("aguia")
        elif opcao3 == "onivoro":
            print("pomba")
    elif opcao2 == "mamifero":
        if opcao3 == "onivoro":
            print("homem")
        elif opcao3 == "herbivoro":
            print("vaca")
elif opcao1 == "invertebrado":
    if opcao2 == "inseto":
        if opcao3 == "hematofago":
            print("pulga")
        elif opcao3 == "herbivoro":
            print("lagarta")
    elif opcao2 == "anelideo":
        if opcao3 == "hematofago":
            print("sanguessuga")
        elif opcao3 == "onivoro":
            print("minhoca")