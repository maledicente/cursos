import json

jogador = {
  "nome": "Luiz",
  "time": "aviadores",
  "vivo": "True",
  "energia": 100,
  "mochila": ["pederneira","corda","linha","arame"],
  "aeronaves": [
    {"tipo": "transporte","habilidade": 80},
    {"tipo": "ataque","habilidade": 100},
    {"tipo": "reconhecimento","habilidade": 50}
  ]
}

for i in jogador["mochila"]:
   print(i)

for i in jogador["aeronaves"]:
   print(i)