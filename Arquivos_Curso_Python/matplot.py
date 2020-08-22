import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,5,11)
y=x*x
print(x)
print(y)
plt.plot(x,y,'r--')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Título')
plt.show()
