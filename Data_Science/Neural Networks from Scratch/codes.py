import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from jupyterthemes import jtplot
jtplot.style(theme='onedork')
jtplot.style(ticks=True, grid=True)
from savefig import *


inputs = np.array([[1.0,2.0,3,2.5],
				   [2,5,-1,2],
				   [-1.5,2.7,3.3,-0.8]])

weights = np.array([[0.2,0.8,-0.5,1],
				    [0.5,-0.91,0.26,-0.5],
				    [-0.26,-0.27,0.17,0.87]])

biases = [2,3,0.5]

output = np.dot(inputs, weights.T) + biases

print(inputs.shape, weights.T.shape, output.shape)