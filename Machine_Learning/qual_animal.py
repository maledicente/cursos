from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import numpy as np
#pelo longo
#perna curta
#faz auau?
porco1=[0,1,0]
porco2=[0,1,1]
porco3=[1,1,0]

cachorro1=[0,1,1]
cachorro2=[0,1,1]
cachorro3=[0,1,1]

treino_x=[porco1,porco2,porco3,cachorro1,cachorro2,cachorro3]
treino_y=[1,1,1,0,0,0] #0 cachorro 1 porco
modelo=LinearSVC()
modelo.fit(treino_x,treino_y)
animal_misterioso=[1,1,1]
misterio1=[1,1,1]
misterio2=[1,1,0]
misterio3=[0,1,1]
modelo.predict([animal_misterioso])
teste_x=[misterio1,misterio2,misterio3]
teste_y=[0,1,1]
previsoes=modelo.predict(teste_x)

previsoes=modelo.predict(teste_x)
print(accuracy_score(teste_y,previsoes))



