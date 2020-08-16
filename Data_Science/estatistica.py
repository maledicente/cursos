from matplotlib import pyplot as plt
from collections import Counter
from random import randint

def median(v):
   """encontra o valor mais ao meio de v"""
   n = len(v)
   sorted_v = sorted(v)
   midpoint = n // 2
   if n % 2 == 1:
      # se for ímpar, retorna o valor do meio
      return sorted_v[midpoint]
   else:
      # se for par, retorna a média dos valores do meio
      lo = midpoint - 1
      hi = midpoint
      return (sorted_v[lo] + sorted_v[hi]) / 2


num_friends = []
for i in range (100):
    num_friends.append(randint(0, 100))

friend_counts = Counter(num_friends)
xs = range(101) # o valor maior é 100
ys = [friend_counts[x] for x in xs] # a altura é somente # de amigos
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histograma da Contagem de Amigos")
plt.xlabel("# de amigos")
plt.ylabel("# de pessoas")
plt.show()

print(median(num_friends))
