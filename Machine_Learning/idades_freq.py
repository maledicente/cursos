# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

idade= ([19, 21, 23, 25, 25, 29, 31, 33, 35, 37, 39, 41, 31, 19,
         40, 34, 28, 32, 29, 34, 27, 27, 36, 29, 37, 31, 29, 33, 
         34, 39, 26, 27, 37, 33, 38, 34, 33, 29, 36, 28, 27, 34,
         28, 27, 30, 28, 37, 37, 32, 36, 34, 38, 29, 30, 20, 30,
         31, 25, 32, 27, 28, 38, 29, 28, 33, 37, 40, 41, 40, 27,
         30, 27, 25, 25, 29, 25, 39, 29, 39, 24, 25, 28, 24, 29, 
         29, 24, 24, 28, 31, 36, 24, 24, 33, 34, 31, 28, 24, 30,
         31, 37, 17, 30, 27, 32, 35, 26, 26, 34, 33, 25, 24, 32,
         32, 22, 30, 25, 32, 25, 21, 20, 30, 29, 18, 23, 23, 35, 
         20, 18, 27, 29, 17, 35, 17, 21, 28, 17, 23, 25, 24, 23,  
         20, 29, 22, 21, 22, 26, 19, 24, 25, 22, 19, 23, 18, 22, 
         35, 30, 28, 27, 29, 29, 22, 25, 22, 29, 26, 22, 19, 22, 
         33, 24, 29, 28, 19, 26, 29, 19, 31, 21, 21, 26, 31, 29])

#Tamanho da amostra
tamanho= len(idade)

# quantidade de Classes (bins)
cl = int(round(tamanho**(1/2),0))

plt.title("Histograma de Idades")
plt.xlabel("Idades")
plt.ylabel("Frequências")

# Range é uma tupla indicando o intervalo das idades. alpha corresponde a saturação da cor
plt.hist(idade, bins = cl, range = ( min(idade), max(idade)), alpha = 0.6, color = 'g')

plt.tight_layout()

plt.show()