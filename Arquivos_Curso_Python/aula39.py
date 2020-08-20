import json

with open('/home/usuario/Documentos/GitHub/cursos/Arquivos_Curso_Python/jogador.json') as f:
  jogador=json.load(f)

def linha():
  print('----------------------------')
 
#Chaves
#for c in jogador:
#	print(c)
#linha()
#itens
#for c in jogador.items():
#	print("\n",c)
#linha()
#valores
#for v in jogador.values():
#	print("\n",v)
#linha()
#nome do jogador
#print(jogador["nome"])

linha()

for a in jogador["aeronaves"]:
	print(a["tipo"] + " - " + str(a["habilidade"]))
  