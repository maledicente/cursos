import pandas as pd
import matplotlib.pyplot as plt

data = [-2, 3, 5, 8, 9, 11, 13, 14, 15, 17, 35]
valores = pd.DataFrame(data)

print(round(valores.describe()), 2)

plt.boxplot(data, showfliers=False, notch=True, patch_artist=False)
plt.title("Valores")
plt.show()
