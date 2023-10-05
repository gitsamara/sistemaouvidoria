from ouvidoria_versao02 import *

def main():
    conn = abrirBancoDados("localhost", "root", "s@M{0511_", "ouvidoria")

    while True:
        print("OUVIDORIA")
        print("Estamos aqui para lhe ajudar! Registre sua manifestação e nós a levaremos ao conhecimento da instância pertinente.")

        print("1. Listar Manifestações")
        print("2. Adicionar Nova Manifestação")
        print("3. Alterar Manifestação")
        print("4. Excluir Manifestação")
        print("5. Sair do Sistema")

        opcao = int(input("Digite a sua opção: "))

        if opcao == 1:
            listar_manifestacoes(conn)
        elif opcao == 2:
            adicionar_manifestacao(conn)
        elif opcao == 3:
            alterar_manifestacao(conn)
        elif opcao == 4:
            excluir_manifestacao(conn)
        elif opcao == 5:
            break
        else:
            print("Opção inválida! Tente outra vez.")

    encerrarBancoDados(conn)
    print("Obrigado por colaborar com nosso sistema! Até mais.")

if __name__ == "__main__":
    main()
