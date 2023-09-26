from operacoesbd import *

conn = abrirBancoDados ("localhost", "root", "s@M{0511_", "ouvidoria")

consultaSqlListagemManifestacoes = "select * from ouvidoria_bd"
listaManifestacoes = listarBancoDados(conn, consultaSqlListagemManifestacoes)

for f in listaManifestacoes:
    print(f)

encerrarBancoDados(conn)
