import os
import pandas as pd
norm = {'Altura': [1.65, 1.85,1.88],
        'Peso': [75, 90,80]}

df = pd.DataFrame(norm)
os.system("clear")
print("-----------------------")
print(df["Altura"]/df["Altura"].mean())
print("-----------------------")
print(df["Peso"]/(df["Peso"].mean()))
