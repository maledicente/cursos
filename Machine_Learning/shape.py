import pandas as pd
df = pd.read_csv('titanic.csv')
arr = df[['Pclass', 'Fare', 'Age']].values
print(arr.shape)