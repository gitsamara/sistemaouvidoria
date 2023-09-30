from operacoesbd import *

opcao = 123
manifestacao = []

conn = abrirBancoDados("localhost", "root", "s@M{0511_", "ouvidoria")

while opcao != 5:
    print("OUVIDORIA")
    print("1 listar, 2 adicionar, 3 alterar, 4 excluir, 5 sair do sistema")
    opcao = int(input("digite a sua opcao: "))

    if opcao == 1:
        print("Lista de Manifestações")
        consultaSqlListagemManifestacoes = "select * from ouvidoria_bd"
        manifestacao = listarBancoDados(conn, consultaSqlListagemManifestacoes)

        for f in manifestacao:
            print(f)

    elif opcao == 2:
        print("Tipo de Manifestação:\n\n 1 reclamação, 2 sugestão, 3 elogio")

        tipoManifestacao = input("digite o tipo de manifestação que você deseja fazer: ")
        assuntoManifestacao = input("digite o assunto: ")
        manifestacao = input("fale aqui: ")

        consultaManifestcao = "insert into ouvidoria_bd (tipo_manifestacao, assunto, manifestacao) values (%s, %s, %s)"
        dados = [tipoManifestacao, assuntoManifestacao, manifestacao]

        insertNoBancoDados(conn, consultaManifestcao, dados)
        print("Manifestacao adicionada com sucesso!")

    elif opcao == 3:
        if (len(manifestacao)) == 0:
            print("Entrada inválida! Verifique a opção escolhida e tente novamente.")

        elif len(manifestacao) > 0:
            print("Portfólio de Manifestações: ")
            for i in range(len(manifestacao)):
                print(i + 1, manifestacao[i])

            codigoManifestacao = int(input("Digite o código da reclamação que deseja alterar: "))

            if codigoManifestacao in range(1, len(manifestacao) + 1):
                novoTexto = input("Digite seu novo texto: ")
                atualizarManifestacao = "update ouvidoria_bd set manifestacao = %s where codigo = %s"
                dadosAtualizacao = (novoTexto, manifestacao [codigoManifestacao - 1][0])
                atualizarBancoDados(conn, atualizarManifestacao, dadosAtualizacao)
                print("Manifestação alterada com sucesso!")

            else:
                print("Número de manifestação inválido! Tente novamente.")

    elif opcao == 4:
        if (len(manifestacao)) == 0:
            print("Entrada inválida! Verifique a opção escolhida e tente novamente.")

        elif len(manifestacao) > 0:
            print("Portfólio de Manifestações: ")
            for i in range(len(manifestacao)):
                print(i + 1, manifestacao[i])

            codigoManifestacao = int(input("Digite o código da reclamação que deseja excluir: "))

            if codigoManifestacao in range(1, len(manifestacao) + 1):
                idManifestacaoExcluir = manifestacao[codigoManifestacao - 1][0]
                excluirManifestacao = "delete from ouvidoria_bd where codigo = %s"
                dadosExclusao = (idManifestacaoExcluir,)
                excluirBancoDados(conn, excluirManifestacao, dadosExclusao)
                manifestacao.pop(codigoManifestacao - 1)
                print("Manifestação excluída!")

    elif opcao != 5:
        print("Opcao invalida! Tente outra vez.")

encerrarBancoDados(conn)
print("Obrigado por colaborar com nosso sistema!")
