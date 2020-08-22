import sqlite3
from sqlite3 import Error

######### Criar conexao
def ConexaoBanco():
   caminho = "/home/usuario/Documentos/GitHub/cursos/Arquivos_Curso_Python/Banco/agenda.db"
   con = None
   try:
      con = sqlite3.connect(caminho)
   except Error as ex:
      print(ex)
   return con
vcon = ConexaoBanco()

nome=input("Digite o nome: ")
tel=input("Digite o telefone: ")
email=input("Digite o E-mail: ")

vsql="INSERT INTO tb_contatos(T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO)VALUES('"+nome+"','"+tel+"','"+email+"')"

def inserir(conexao,sql):
	try:
		c = conexao.cursor()
		c.execute(sql)
		print("Registro inserido")
		conexao.commit()
	except Error as ex:
		print(ex)

inserir(vcon,vsql)


