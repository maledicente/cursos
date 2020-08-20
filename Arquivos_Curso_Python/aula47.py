import sqlite3
from sqlite3 import Error

######### Criar conexao
def ConexaoBanco():
	caminho="/home/usuario/Documentos/GitHub/cursos/Arquivos_Curso_Python/Banco/agenda.db"
	con=None
	try:
		con=sqlite3.connect(caminho)
	except Error as ex:
		print(ex)
	return con

vcon=ConexaoBanco()
###########
vsql="""CREATE TABLE tb_contatos(
			N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
			T_NOMECONTATO VARCHAR(30),
			T_TELEFONECONTATO VARCHAR(30),
			T_EMAILCONTATO VARCHAR(30)
		);"""

def criarTabela(conexao,sql):
	try:
		c=conexao.cursor()
		c.execute(sql)
		print("Tabela criada!")
	except Error as Ex:
		print(Ex)

criarTabela(vcon,vsql)

vcon.close()