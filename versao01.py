#Samara Sales e Vagner Carvalho
opcao = 1

reclamacoes = []

while opcao != 5:
    print("Sistema de Ouvidoria Aula de Abellardo")
    print()
    print("Digite 1 para acessar o Portfólio de Reclamações;")
    print("Digite 2 para cadastrar uma nova reclamação;")
    print("Digite 3 parar excluir uma reclamação;")
    print("Digite 4 para alterar sua reclamação;")
    print("Digite 5 para sair do sistema.")
    print()
    opcao = int(input("Digite sua opção: "))


    if opcao == 1:
        if (len(reclamacoes)) == 0:
            print("Portfólio vazio!")
        else:
            print("Portfólio de Reclamações: ")

            for i in range(len(reclamacoes)):
                print(i + 1, reclamacoes[i])


    elif opcao == 2:
        novaReclamacao = input("Registe sua reclamação: ")
        reclamacoes.append(novaReclamacao)
        print(
            "Sua reclamação foi registrada com sucesso! \nObrigada pela sua participação. Agora levaremos sua manifestação ao conhecimento do órgão competente.")


    elif opcao == 3:
        if (len(reclamacoes)) == 0:
            print("Entrada inválida! Verifique a opção escolhida e tente novamente.")

        elif len(reclamacoes) > 0:
            print("Portfólio de Reclamações: ")
            for i in range(len(reclamacoes)):
                print(i + 1, reclamacoes[i])

            codigoReclamacao = int(input("Digite o código da reclamação que deseja excluir: "))
            reclamacoes.pop(codigoReclamacao - 1)
            print("Reclamação excluída!")


    elif opcao == 4:
        if (len(reclamacoes)) == 0:
            print("Entrada inválida! Verifique a opção escolhida e tente novamente.")

        elif len(reclamacoes) > 0:
            print("Portfólio de Reclamações: ")
            for i in range(len(reclamacoes)):
                print(i + 1, reclamacoes[i])

            codigoReclamacao = int(input("Digite o código da reclamação que deseja alterar: "))
            if codigoReclamacao in range(1, len(reclamacoes) + 1):
                novoTexto = input("Digite seu novo texto: ")
                reclamacoes[codigoReclamacao - 1] = novoTexto
                print("Reclamação alterada com sucesso!")
            else:
                print("Código de reclamação inválido! Tente novamente.")


    elif opcao == 5:
        print("Bye!")


    else:
        print("Opção inválida! Verifique a opção escolhida e tente outra vez.")

print("Até mais.")
