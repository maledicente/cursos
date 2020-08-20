import os
from pathlib import Path
import re

mypath = str(Path().absolute()) + "/"
filename = input("Nome do arquivo.txt: ")
local= mypath + filename

os.system("clear")

os.remove(local)