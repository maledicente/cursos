import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('titanic.csv')
plt.scatter(df['Age'], df['Fare'], c=df['Pclass'])
plt. xlabel('Age')
plt. ylabel('Tarifa')
plt.plot([0, 80], [85, 5])