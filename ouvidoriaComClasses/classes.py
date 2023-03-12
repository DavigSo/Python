class Reclamacoes:
    reclamacoes = []

    def addReclamacoes(self, rec):
        self.reclamacoes.append(rec)

    def getReclamacoes(self):
        for i, rec in enumerate(self.reclamacoes):
            print(i + 1, "-", rec)

    def deleteReclamacoes(self):
        print("Deseja excluir uma reclamação ou todas?")
        print("0 - Excluir todas")
        print("1 - Excluir uma")

        confirmacao = int(input())

        if confirmacao == 0:
            self.reclamacoes.clear()
            print("Todas as reclamações foram apagadas.")
        elif confirmacao == 1:
            print("Apagar reclamação especifica")

            for i, rec in enumerate(self.reclamacoes):
                print(i + 1, "-", rec)

            indice = int(input("Qual a reclamação: "))
            self.reclamacoes.pop(indice - 1)
            print("Reclamação removida com sucesso!")

    def setReclamacoes(self):
        for i, rec in enumerate(self.reclamacoes):
            print(i + 1, "-", rec)

        indice = int(input("Qual reclamação deseja editar? "))
        novaRec = input("Digite sua nova reclamação:\n")

        self.reclamacoes[indice - 1] = novaRec


class Elogios:
    elogios = []

    def addElogios(self, gio):
        self.elogios.append(gio)

    def getElogios(self):
        for i, gio in enumerate(self.elogios):
            print(i + 1, "-", gio)

    def deleteElogios(self):
        print("Deseja excluir um Elogio ou todos?")
        print("0 - Excluir todos")
        print("1 - Excluir um")

        confirmacao = int(input())

        if confirmacao == 0:
            self.elogios.clear()
            print("Todos os Elogios foram apagados.")
        elif confirmacao == 1:
            print("Apagar Elogio especifico")

            for i, gio in enumerate(self.elogios):
                print(i + 1, "-", gio)

            indice = int(input("Qual a Elogios: "))
            self.elogios.pop(indice - 1)
            print("Elogio removido com sucesso!")

    def setElogios(self):
        for i, gio in enumerate(self.elogios):
            print(i + 1, "-", gio)

        indice = int(input("Qual Elogio deseja editar? "))
        novoGio = input("Digite seu novo Elogio:\n")

        self.elogios[indice - 1] = novoGio
