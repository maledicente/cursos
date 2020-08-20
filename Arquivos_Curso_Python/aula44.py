import os

filename = str(input("Nome do arquivo.txt: "))
f=open("/home/usuario/Documentos/GitHub/cursos/Arquivos_Curso_Python/"+filename,"at")

os.system("clear")
txt=input("Digite um texto: ")
f.write(txt+"\n")

f.close()
