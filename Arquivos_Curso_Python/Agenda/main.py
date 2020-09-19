import os
import sqlite3
from sqlite3 import Error

##Conexao
def ConexaoBanco():
   caminho = "/home/usuario/Documentos/GitHub/cursos/Arquivos_Curso_Python/Banco/agenda.db"
   con = None
   try:
      con = sqlite3.connect(caminho)
   except Error as ex:
      print(ex)
   return con

vcon = ConexaoBanco()

def menuPrincipal():
	os.system("clear")
	print("1 - Inserir Novo Registro")
	print("2 - Deletar Registro")
	print("3 - Atualizar Registro")
	print("4 - Consultar Registro por ID")
	print("5 - Consultar Registro por Nome")
	print("6 - Sair")

def menuInserir():
	print()

def menuDeletar():
	print()

def menuAtualizar():
	print()

def menuConsultarId():
	print()

def menuConsultarNomes():
	print()

opc=0
while opc !=6:
	menuPrincipal()
	opc=int(input("Digite uma opcão: "))
	if opc==1:
		menuInserir()
	elif opc==2:
		menuDeletar()
	elif opc==3:
		menuAtualizar()
	elif opc==4:
		menuConsultarId()
	elif opc==5:
		menuConsultarNome()
	elif opc==6:
		os.system("clear")
		print("Programa finalizado")
	else:
		os.system("clear")
		print("Opção invalida")
		os.system("pause")
os.system("clear")