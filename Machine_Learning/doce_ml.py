import pandas as pd
from sklearn.model_selection import  train_test_split
from sklearn.ensemble import ExtraTreesClassifier

arquivo = pd.read_csv("wine_dataset.csv")

arquivo['style'] = arquivo['style'].replace('red', 0)
arquivo['style'] = arquivo['style'].replace('white', 1)

y = arquivo['style']
x = arquivo.drop('style', axis=1)

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size= 0.3)

#Criação de modelo:
modelo = ExtraTreesClassifier()
modelo.fit(x_treino, y_treino)

#Imprimindo resultados
resultado = modelo.score(x_teste, y_teste)
print("Acurácia: ", resultado)

y_teste[400:403]
x_teste[400:403]
previsoes = modelo.predict(x_teste[400:403])
print(previsoes)

