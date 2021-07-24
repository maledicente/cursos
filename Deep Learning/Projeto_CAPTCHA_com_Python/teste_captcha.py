from keras.models import load_model
from helpers import resize_to_fit
from imutils import paths
import numpy as np
import cv2
import pickle
from tratar_captcha import tratar_imagens

def quebrar_captcha():
	# import modelo treinado e tradutor
	with open('rotulos_modelo.txt', 'rb') as arquivo_tradutor:
		lb = pickle.load(arquivo_tradutor)

	modelo = load_model('modelo_treinado.hdf5')

	# Testar modelo
	tratar_imagens("resolver_captcha", "resolver_captcha")

	############
	arquivos = list(paths.list_images('resolver_captcha'))
	for arquivo in arquivos:
		imagem = cv2.imread(arquivo)
		imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
		#preto e branco
		_, nova_imagem = cv2.threshold(imagem, 0, 255, cv2.THRESH_BINARY_INV)

		# encontrar contornos das letras
		contornos, _ = cv2.findContours(nova_imagem, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

		regiao_letras = []

		# filtrar contornos que sao letras
		for contorno in contornos:
			(x, y, largura, altura) = cv2.boundingRect(contorno)
			area = cv2.contourArea(contorno)
			if area > 115:
				regiao_letras.append((x, y, largura, altura))

		regiao_letras = sorted(regiao_letras, key=lambda x: x[0])

		# desenhar contornos e separar letras em arquivos individuais
		imagem_final = cv2.merge([imagem] * 3)
		previsao = []

		i=0
		for retangulo in regiao_letras:
			x, y, largura, altura = retangulo
			imagem_letra = imagem[y-2:y+altura+2, x-2:x+largura+2]

			imagem_letra = resize_to_fit(imagem_letra, 20, 20)
			imagem_letra = np.expand_dims(imagem_letra, axis=2)
			imagem_letra = np.expand_dims(imagem_letra, axis=0)

			letra_prevista = modelo.predict(imagem_letra)
			letra_prevista = lb.inverse_transform(letra_prevista)[0]
			previsao.append(letra_prevista)

			# Desenhar letras prevista
		texto_previsao = "".join(previsao)
		print(texto_previsao)
		return texto_previsao

if __name__ == "__main__":
	quebrar_captcha()

"""
i+=1
			nome_arquivo = os.path.basename(arquivo).replace('.png', f'letra{i}.png')
			cv2.imwrite(f'letras/{nome_arquivo}', imagem_letra)			
			cv2.rectangle(imagem_final,(x-2, y-2), (x+largura+2, y+altura+2), (0,255,0),1)
		#nome_arquivo = os.path.basename(arquivo)
		#cv2.imwrite(f'{identificado}/{nome_arquivo}', imagem_final)
"""
