from operacoesbd import *

def listar_manifestacoes(conn):
    consulta_sql = "select * from ouvidoria_bd"
    manifestacoes = listarBancoDados(conn, consulta_sql)

    if not manifestacoes:
        print("Nenhuma manifestação registrada.")
    else:
        print("Portfólio de Manifestações Registradas no Sistema:")
        for i, manifestacao in enumerate(manifestacoes, start=1):
            print(f"{i}. Tipo de Manifestação: {manifestacao[1]} | Assunto: {manifestacao[2]} | Registro: {manifestacao[3]}")

def adicionar_manifestacao(conn):
    print("Registre aqui sua manifestação de acordo com as categorias a seguir: ")
    print("\nTIPO DE MANIFESTAÇÃO\n")
    print("* Reclamação")
    print("* Sugestão")
    print("* Elogio\n")

    tipo_manifestacao = input("Digite o tipo de manifestação que você deseja fazer: ")
    assunto_manifestacao = input("Digite o assunto: ")
    texto_manifestacao = input("Fale aqui: ")

    consulta_manifestacao = "insert into ouvidoria_bd (tipo_manifestacao, assunto, manifestacao) values (%s, %s, %s)"
    dados = [tipo_manifestacao, assunto_manifestacao, texto_manifestacao]

    insertNoBancoDados(conn, consulta_manifestacao, dados)
    print("Manifestação adicionada com sucesso!")

def alterar_manifestacao(conn):
    listar_manifestacoes(conn)
    codigo_manifestacao = int(input("Digite o código da manifestação que deseja alterar: "))

    consulta_sql = "select * from ouvidoria_bd"
    manifestacoes = listarBancoDados(conn, consulta_sql)

    if codigo_manifestacao in range(1, len(manifestacoes) + 1):
        novo_texto = input("Digite seu novo texto: ")
        atualizar_manifestacao = "update ouvidoria_bd set manifestacao = %s where codigo = %s"
        dados_atualizacao = (novo_texto, manifestacoes[codigo_manifestacao - 1][0])
        atualizarBancoDados(conn, atualizar_manifestacao, dados_atualizacao)
        print("Manifestação alterada com sucesso!")
    else:
        print("Número de manifestação inválido! Tente novamente.")

def excluir_manifestacao(conn):
    listar_manifestacoes(conn)
    codigo_manifestacao = int(input("Digite o código da manifestação que deseja excluir: "))

    consulta_sql = "select * from ouvidoria_bd"
    manifestacoes = listarBancoDados(conn, consulta_sql)

    if codigo_manifestacao in range(1, len(manifestacoes) + 1):
        id_manifestacao_excluir = manifestacoes[codigo_manifestacao - 1][0]
        excluir_manifestacao = "delete from ouvidoria_bd where codigo = %s"
        dados_exclusao = (id_manifestacao_excluir,)
        excluirBancoDados(conn, excluir_manifestacao, dados_exclusao)
        manifestacoes.pop(codigo_manifestacao - 1)
        print("Manifestação excluída!")
    else:
        print("Número de manifestação inválido! Tente novamente.")
        