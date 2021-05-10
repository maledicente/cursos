import numpy as np 
#Entropia 
#Quantifica a quantidade de (toda possível) informação em uma variavel
#Número de bits necessarios para transmitir um evento selecionado aleatoriamente a partir de uma distribuição de probabilidade

def entropia(d):
  H=0
  for i in d.values():
    H+=(i * - np.log2(i))
  print("Quantidade de informação: {:.3f} bits".format(H))

def entropia_cruzada(d1, d2):
  H=0
  for p, q in zip(d1.values(),d2.values()):
    H+=(p * - np.log2(q))
  print("Entropia relativa das duas distribuiçoes de probabilidade: {:.3f} bits".format(H))

#Variavel
x = 'Bitcoin vai cair?'

#Distribuição de probabilidade
dist = {"cair": 0.5, "subir": 0.3, "estagnar": 0.2}
dist2 = {"cair": 0.4, "subir": 0.3, "estagnar": 0.3}
#dist3 = {"cair": 0.999, "subir": 0.0005, "estagnar": 0.0005}

#entropia(dist)
entropia_cruzada(dist, dist2)
