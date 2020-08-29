import numpy as np

# Primeira reta
m = 7
b = 1
L = 0.0000001  # Learning Rate
iteracoes = 1000

# Criando o Gradiente Descendente
for i in range(iteracoes):
   Y_pred = m * X + b  # Valor atual da reta
   derivadam = np.sum(*2 * X * (Y_pred - y))  # Derivada da função de custo em relação a m
   derivadab = np.sum(2 * (Y_pred - y))  # derivada da função de custo em relação a b
   m = m + derivadam * L  # Atualiza m
   b = b + derivadab * L
print('Valor: ', m, 'valor b:', b)
