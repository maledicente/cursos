import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
jtplot.style(theme='onedork')
jtplot.style(ticks=True, grid=True)
from savefig import *


def f(x):
	return 2*x**2

x = np.arange(0,5,0.001)
y = f(x)

plt.plot(x, y)

colors = ['k', 'g', 'r', 'b', 'c']

def approximate_tangent_line(x, approximate_derivative, b):
	return approximate_derivative * x + b

for i in range(5):
	p2_delta = 0.0001
	x1 = i
	x2 = x1 + p2_delta

	y1 = f(x1)
	y2 = f(x2)

	print((x1, y1), (x2, y2))

	approximate_derivative  =  (y2 -  y1) /  (x2 -  x1)
	b = y2 - approximate_derivative * x2

	to_plot = [x1 - 0.9, x1, x1 + 0.9]
	plt.scatter(x1, y1, c=colors[i])
	plt.plot(to_plot, [approximate_tangent_line(point, approximate_derivative, b) 
		for point in to_plot], c = colors[i])

	print('Approximate derivative for f(x)', f'where x = {x1} is {approximate_derivative}')

plt.title("Values of 2*x^2")
plt.xlabel("Values of x")
plt.ylabel("Values of f(x)")
save_fig('Approximate derivative')
plt.show()




#print('Derivada %.0fx' % approximate_derivative)