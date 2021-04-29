#Perceptron de uma camada
import numpy as np 

entradas = np.array([1, 9, 5])
pesos = np.array([0.8, 0.1, 0])

'''def soma(e,p):
	s = 0
	for i in range(3):
		s += e[i] * p[i]
	return s'''
def Soma(e,p):
	return e.dot(p)

s = Soma(entradas, pesos)
print(s)

def stepFunction(s):
	if (s >= 1):
		return 1
	return 0
	
saida = stepFunction(s)	
print(saida)