from operacoesbd import *

conn = abrirBancoDados ("localhost", "root", "s@M{0511_", "ouvidoria")

tipoManifestacao = input("digite o tipo de manifestação que você deseja fazer: ")
assuntoManifestacao = input("digite o assunto: ")
manifestacao = input("fale aqui: ")

consultaManifestcao = "insert into ouvidoria_bd (tipo_manifestacao, assunto, manifestacao) values (%s, %s, %s)"
dados = [tipoManifestacao, assuntoManifestacao, manifestacao]

insertNoBancoDados(conn, consultaManifestcao, dados)

encerrarBancoDados(conn)
