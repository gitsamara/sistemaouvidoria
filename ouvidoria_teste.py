from operacoesbd import *

opcao = 123
manifestacao = []

conn = abrirBancoDados("localhost", "root", "s@M{0511_", "ouvidoria")

while opcao != 3:
    print("OUVIDORIA")
    print("1 listar, 2 adicionar reclamacao, 3 sair do sistema")
    opcao = int(input("digite a sua opcao: "))

    if opcao == 1:
        print("Lista de Reclamcoes")
        consultaSqlListagemManifestacoes = "select * from ouvidoria_bd"
        manifestacao = listarBancoDados(conn, consultaSqlListagemManifestacoes)

        for f in manifestacao:
            print(f)

    elif opcao == 2:
        tipoManifestacao = input("digite o tipo de manifestação que você deseja fazer: ")
        assuntoManifestacao = input("digite o assunto: ")
        manifestacao = input("fale aqui: ")

        consultaManifestcao = "insert into ouvidoria_bd (tipo_manifestacao, assunto, manifestacao) values (%s, %s, %s)"
        dados = [tipoManifestacao, assuntoManifestacao, manifestacao]

        insertNoBancoDados(conn, consultaManifestcao, dados)
        print("Manifestacao adicionada com sucesso!")

    elif opcao == 3:
        print("Opcao invalida! Tente outra vez.")

encerrarBancoDados(conn)
print("Obrigado por colaborar com nosso sistema!")
