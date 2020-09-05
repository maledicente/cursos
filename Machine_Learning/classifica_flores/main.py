import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv("iris.csv")
#print(df.columns)
print(df.describe())
sb.pairplot(df,hue='target')
