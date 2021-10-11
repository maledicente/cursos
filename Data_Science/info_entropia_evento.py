import numpy as np

print("######### Entropia #########")
print("-" * 28)

variavel = input("Entre com a váriavel: ")

num_items = int(input("Entre com o numero de items da distribuição: "))

distribuicao = {}

for i in range(num_items):
	item = input(f"\nEntre com o nome do {i+1}-item: ")
	probabilidade = float(input("Qual a probabilidade do item? (porcentagem): "))/100
	distribuicao[item] = probabilidade

info = 0

for value in distribuicao.values():
	info += (value * - np.log2(value))
	
print("\nEntropia da variavel' {}' é: {:.3f} bits".format(variavel, info))
