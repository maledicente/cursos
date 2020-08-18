from matplotlib import pylab as plt
import numpy as np

meses = [1,2,3,4,5,6,7,8,9,10,11,12]
peso = [70,72,71,70,68,69,67,69,70,71,72,73]
altura = 1.7
imc = np.around(list(np.array(peso)/pow(altura,2)),2)


plt.plot(meses,imc,color='green',marker='o',linestyle='solid')

plt.title("Peso ao longo do tempo")

plt.ylabel("IMC")
plt.xlabel("Meses")
plt.axis([1, 12, 18, 30]) # [xmin, xmax, ymin, ymax]
plt.show()

for i in imc:
   print(i)



