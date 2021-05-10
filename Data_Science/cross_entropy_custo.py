import numpy as np 

# L(ŷ,y) = - ∑yi*log(ŷi)

def entropia_custo(d1, d2):
  H=0
  for p, q in zip(d1, d2):
    H+=(p * - np.log2(q))
  print("Custo: {:.3f} bits".format(H))

valor_real = [1,0,0]
#valor_estimado = [0.6,0.15,0.25]
valor_estimado = [0.9,0.05,0.05]

entropia_custo(valor_real, valor_estimado)

from scipy.stats import entropy

def cross_entropy_via_scipy(x, y):
    return  entropy(x) + entropy(x, y)

m = cross_entropy_via_scipy(valor_real, valor_estimado)
print(m)