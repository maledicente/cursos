import os
from pathlib import Path

mypath = str(Path().absolute()) + "/"
filename = input("Nome do arquivo.txt: ")
local= mypath + filename
f = open(local, "wt")
print(local)

txt=input("Digite um texto: ")
f.write(txt)

os.system("clear")

f.close()
