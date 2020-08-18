import json

jogador_j='{"nome":"Luiz Paulo","time":"aviadores","vivo":"True","energia": 100,"mochila": ["pederneira","corda","linha","arame"],"aeronaves": [{"tipo": "transporte","habilidade": 80},{"tipo": "ataque","habilidade": 100},{"tipo": "reconhecimento","habilidade": 50}]}'

jogador=json.loads(jogador_j)

#Chaves
#for c in jogador:
#	print(c)

#itens
#for c in jogador.items():
#	print("\n",c)

#valores
#for v in jogador.values():
#	print("\n",v)

#nome do jogador
#print(jogador["nome"])

for a in jogador["aeronaves"]:
	print(a["tipo"] + " - " + str(a["habilidade"]))