import cv2
from PIL import Image
import os 
import glob

def tratar_imagens(origem, destino='img_tratada'):
	arquivos = glob.glob(f"{origem}/*")

	for arquivo in arquivos:
		imagem = cv2.imread(arquivo)
		#Transformar a imagem em escala de cinza
		imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

		_, imagem_t = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_TRUNC or cv2.THRESH_OTSU)
		nome_arquivo = os.path.basename(arquivo)
		cv2.imwrite(f'{destino}/{nome_arquivo}', imagem_t)

	arquivos = glob.glob(f"{destino}/*")
	
	for arquivo in arquivos:
		imagem = Image.open(arquivo)
		imagem = imagem.convert("P")
		imagem2 = Image.new("P", imagem.size, 255)

		for x in range(imagem.size[1]):
			for y in range(imagem.size[0]):
				cor_pixel = imagem.getpixel((y, x))
				if cor_pixel < 115:
					imagem2.putpixel((y, x), 0)
		nome_arquivo = os.path.basename(arquivo)
		imagem2.save(f'{destino}/{nome_arquivo}')

if __name__ == "__main__":
	tratar_imagens('bdcaptcha')

'''
#Metodos Opencv
metodos = [
	cv2.THRESH_BINARY,
	cv2.THRESH_BINARY_INV,
	cv2.THRESH_TRUNC,
	cv2.THRESH_TOZERO,
	cv2.THRESH_TOZERO_INV,
]
imagem = cv2.imread("telanova0.png")

#Transformar a imagem em escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

i = 0
for metodo in metodos:
	i+=1
	_, imagem_t = cv2.threshold(imagem_cinza, 127, 255, metodo or cv2.THRESH_OTSU)
	cv2.imwrite(f'imagem_t_{i}.png', imagem_t)

im = Image.open("imagem_t_3.png")
im = im.convert("P") # Escala de cinza
im2 = Image.new("P", im.size, 255)

for x in range(im.size[1]):
	for y in range(im.size[0]):
		cor_pixel = im.getpixel((y, x))
		if cor_pixel < 115:
			im2.putpixel((y, x), 0)

im2.save("final/imagemfinal.png")
print(im2.size)'''

