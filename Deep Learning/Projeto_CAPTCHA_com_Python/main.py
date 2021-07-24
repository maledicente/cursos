
import cv2
import os 
import numpy as np
import pandas as pd
import time
import pickle
from imutils import paths
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Flatten, Dense
from helpers import resize_to_fit

"""Passos:
[
	1 - Capturar versoes de imagens, 
	2 - Remover ruídos,
	3 - Separar Imagens em Letras,
	4 - Categorizar as Letras para treino,
	5 - Ajuste manual inteligente,
	6 - Treinar a IA,
	7 - Testar a quebra de captcha
]"""

dados = []
rotulos = []
pasta_base_imagens = "base_letras"

imagens = paths.list_images(pasta_base_imagens)

print('\nIniciando transformação de imagens para treino...')
start_time = time.time()

for arquivo in imagens:
	rotulo = arquivo.split(os.path.sep)[-2]
	imagem = cv2.imread(arquivo)
	imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

	# Padronizar imagens 20x20
	imagem = resize_to_fit(imagem, 20, 20)

	# Adicionar dimensao para o keras ler a imagem
	imagem = np.expand_dims(imagem, axis=2)
	rotulos.append(rotulo)
	dados.append(imagem)

dados = np.array(dados, dtype='float') / 255
rotulos = np.array(rotulos)

print('Preparação terminada!')
print("--- %s seconds ---" % (time.time() - start_time))

# Separacao dados treino (80%) e teste (20%)
(X_train, x_test, Y_train, y_test) = train_test_split(dados, rotulos, test_size=0.25, random_state=0)

# Converter com one-hot encoding
lb = LabelBinarizer().fit(Y_train)
Y_train = lb.transform(Y_train)
y_test = lb.transform(y_test)

# Salvar labelbinarizer em um arquivo pickle

with open('rotulos_modelo.txt', 'wb') as arquivo_pickle:
	pickle.dump(lb, arquivo_pickle)

# Treinar IA
modelo = Sequential()

# Criar camadas da rede neural
modelo.add(Conv2D(20, (5, 5), padding='same', input_shape=(20,20,1), activation='relu'))
modelo.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

# Segunda camada
modelo.add(Conv2D(50, (5,5), padding='same', activation='relu'))
modelo.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

# Terceira camada com Flatten
modelo.add(Flatten())
modelo.add(Dense(500, activation='relu'))

# Camada de saíde
modelo.add(Dense(26, activation='softmax'))

print('\nCompilando modelo...')
start_time = time.time()

# Commpliar
modelo.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

end_time = time.monotonic()
print('Compilação terminada!')
print("--- %s seconds ---\n" % (time.time() - start_time))

modelo.fit(X_train, Y_train, validation_data=(x_test, y_test), batch_size=26, epochs=10, verbose=1)

# Salvar modelo
modelo.save('modelo_treinado.hdf5')
print()