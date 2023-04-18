from operacoesbd import *


class Reclamacoes:
    idReclamacao = []
    tipoReclamacao = []
    descricaoReclamacao = []

    def addReclamacoes(self, rec):
        conexao = openDB("localhost", "root", "root", "ouvidoria")
        codigosql = "INSERT INTO ocorrencias(tipo, descricao) VALUES (%s, %s)"
        dados = ("Reclamação", rec)
        insertInDB(conexao, codigosql, dados)

        closeDB(conexao)

    def getReclamacoes(self):
        self.idReclamacao = []
        self.tipoReclamacao = []
        self.descricaoReclamacao = []

        conexao = openDB("localhost", "root", "root", "ouvidoria")
        codigoSql = 'SELECT * FROM ocorrencias WHERE tipo="Reclamação"'
        listaReclamacoes = listDB(conexao, codigoSql)

        for itemDB in listaReclamacoes:
            self.idReclamacao.append(itemDB[0])
            self.tipoReclamacao.append(itemDB[1])
            self.descricaoReclamacao.append(itemDB[2])

        for i in range(len(self.idReclamacao)):

            print(
                f"{ i + 1} - {self.tipoReclamacao[i]} - {self.descricaoReclamacao[i]}"
            )

        closeDB(conexao)

    def deleteReclamacoes(self):
        conexao = openDB("localhost", "root", "root", "ouvidoria")
        self.getReclamacoes()

        indice = int(input("Qual a reclamação: "))
        codigoSql = "DELETE FROM ocorrencias WHERE id = %s"

        id = self.idReclamacao[indice - 1]
        dados = (id,)

        deleteInDB(conexao, codigoSql, dados)
        print("Reclamação removida com sucesso!")

        closeDB(conexao)

    def setReclamacoes(self):
        conexao = openDB("localhost", "root", "root", "ouvidoria")
        self.getReclamacoes()

        indice = int(input("Qual reclamação deseja editar? "))
        novaRec = input("Digite sua nova reclamação:\n")

        id = self.idReclamacao[indice - 1]

        codigoSql = "UPDATE ocorrencias SET descricao = %s WHERE id = %s"
        dados = (novaRec, id)

        updateDB(conexao, codigoSql, dados)

        print("Editado com sucesso")


class Elogios:
    idElogio = []
    tipoElogio = []
    descricaoElogio = []

    def addElogios(self, gio):
        conexao = openDB("localhost", "root", "root", "ouvidoria")
        codigosql = "INSERT INTO ocorrencias(tipo, descricao) VALUES (%s, %s)"
        dados = ("Elogio", gio)
        insertInDB(conexao, codigosql, dados)

        closeDB(conexao)

    def getElogios(self):
        self.idElogio = []
        self.tipoElogio = []
        self.descricaoElogio = []

        conexao = openDB("localhost", "root", "root", "ouvidoria")
        codigoSql = 'SELECT * FROM ocorrencias WHERE tipo="Elogio"'
        listaElogios = listDB(conexao, codigoSql)

        for itemDB in listaElogios:
            self.idElogio.append(itemDB[0])
            self.tipoElogio.append(itemDB[1])
            self.descricaoElogio.append(itemDB[2])

        for i in range(len(self.idElogio)):

            print(
                f"{ i + 1} - {self.tipoElogio[i]} - {self.descricaoElogio[i]}")

        closeDB(conexao)

    def deleteElogios(self):
        conexao = openDB("localhost", "root", "root", "ouvidoria")
        self.getElogios()

        indice = int(input("Qual o elogio: "))
        codigoSql = "DELETE FROM ocorrencias WHERE id = %s"

        id = self.idElogio[indice - 1]
        dados = (id,)

        deleteInDB(conexao, codigoSql, dados)
        print("Elogio removido com sucesso!")

        closeDB(conexao)

    def setElogios(self):
        conexao = openDB("localhost", "root", "root", "ouvidoria")
        self.getElogios()

        indice = int(input("Qual elogio deseja editar? "))
        novoGio = input("Digite seu novo elogio:\n")

        id = self.idElogio[indice - 1]

        codigoSql = "UPDATE ocorrencias SET descricao = %s WHERE id = %s"
        dados = (novoGio, id)

        updateDB(conexao, codigoSql, dados)

        print("Editado com sucesso")
