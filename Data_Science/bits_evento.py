import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

def info(evento):
		b = - np.log2(evento)
		print("Número de bits para codificar e transmitir o evento: {:.3f} bit. ".format(b))

event = np.log2(np.arange(0,1,0.1))*-1

plt.figure(figsize=(10,6))
plt.plot(np.arange(0,1,0.1),event)
plt.ylabel("Informação")
plt.xlabel("Probabilidade")
plt.show()