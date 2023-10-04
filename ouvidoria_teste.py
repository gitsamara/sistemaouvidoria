from operacoesbd import *

opcao = 123
manifestacao = []

conn = abrirBancoDados("localhost", "root", "s@M{0511_", "ouvidoria")

while opcao != 5:
    print("OUVIDORIA")
    print("Estamos aqui para lhe ajudar! Registre sua manifestação e nós a levaremos ao conhecimento da instância pertinente.")

    print("1. Listar Manifestações")
    print("2. Adicionar Nova Manifestação")
    print("3. Alterar Manifestação")
    print("4. Excluir Manifestação")
    print("5. Sair do Sistema")

    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        print("Portfólio de Manifestações Registradas no Sistema: ")
        consultaSqlListagemManifestacoes = "select * from ouvidoria_bd"
        manifestacao = listarBancoDados(conn, consultaSqlListagemManifestacoes)

        for f in range (len(manifestacao)):
            print(f + 1, ". Tipo de Manifestação: " ,manifestacao[f][1], "| Assunto: ", manifestacao[f][2], "| Registro: ", manifestacao [f][3])

    elif opcao == 2:
        print("Registre aqui sua manifestação de acordo com as categorias a seguir: ")
        print("\nTIPO DE MANIFESTAÇÃO\n")
        print("* Reclamação")
        print("* Sugestão")
        print("* Elogio\n")

        tipoManifestacao = input("Digite o tipo de manifestação que você deseja fazer: ")
        assuntoManifestacao = input("Digite o assunto: ")
        manifestacao = input("Fale aqui: ")

        consultaManifestcao = "insert into ouvidoria_bd (tipo_manifestacao, assunto, manifestacao) values (%s, %s, %s)"
        dados = [tipoManifestacao, assuntoManifestacao, manifestacao]

        insertNoBancoDados(conn, consultaManifestcao, dados)
        print("Manifestacao adicionada com sucesso!")

    elif opcao == 3:
        if (len(manifestacao)) == 0:
            print("Entrada inválida! Verifique a opção escolhida e tente novamente.")

        elif len(manifestacao) > 0:
            print("Portfólio de Manifestações: ")
            for f in range(len(manifestacao)):
                print(f + 1, ". Tipo de Manifestação: ", manifestacao[f][1], "| Assunto: ", manifestacao[f][2], "| Registro: ", manifestacao[f][3])

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
            for f in range(len(manifestacao)):
                print(f + 1, ". Tipo de Manifestação: ", manifestacao[f][1], "| Assunto: ", manifestacao[f][2], "| Registro: ", manifestacao[f][3])

            codigoManifestacao = int(input("Digite o código da reclamação que deseja excluir: "))

            if codigoManifestacao in range(1, len(manifestacao) + 1):
                idManifestacaoExcluir = manifestacao[codigoManifestacao - 1][0]
                excluirManifestacao = "delete from ouvidoria_bd where codigo = %s"
                dadosExclusao = (idManifestacaoExcluir,)
                excluirBancoDados(conn, excluirManifestacao, dadosExclusao)
                manifestacao.pop(codigoManifestacao - 1)
                print("Manifestação excluída!")

            else:
                print("Número de manifestação inválido! Tente novamente.")

    elif opcao != 5:
        print("Opcao invalida! Tente outra vez.")

encerrarBancoDados(conn)
print("Obrigado por colaborar com nosso sistema! Até mais.")