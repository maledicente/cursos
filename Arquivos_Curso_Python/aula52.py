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

nome = input("Digite o nome: ")
tel = input("Digite o telefone: ")
email = input("Digite o E-mail: ")

vsql = "INSERT INTO tb_contatos(T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO)VALUES('" + nome + "','" + tel + "','" + email + "')"


def inserir(conexao, sql):
   try:
      c = conexao.cursor()
      c.execute(sql)
      print("Registro inserido")
      conexao.commit()
   except Error as ex:
      print(ex)


inserir(vcon, vsql)


def deletar(conexao, sql):
   try:
      c = conexao.cursor()
      c.execute(sql)
      conexao.commit()
   except Error as ex:
      print(ex)
   finally:
      print("Registro removido!")


vsql = "DELETE FROM tb_contatos WHERE N_IDCONTATO=1"


# deletar(vcon,vsql)

def atualizar(conexao, sql):
   try:
      c = conexao.cursor()
      c.execute(sql)
      conexao.commit()
   except Error as ex:
      print(ex)
   finally:
      print("Registro atualizado!")


vsql = "UPDATE tb_contatos SET T_NOMECONTATO='Luiz Paulo' WHERE N_IDCONTATO=2"

atualizar(vcon, vsql)

def consulta(conexao, sql):
      c = conexao.cursor()
      c.execute(sql)
      resultado=c.fetchall()
      return  resultado

vsql="SELECT * FROM tb_contatos WHERE N_IDCONTATO=5"
res = consulta(vcon,vsql)

for i in res:
   print(i)