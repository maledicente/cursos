import math

def info(evento):
		b = - math.log2(evento)
		print("Número de bits para codificar e transmitir o evento: {:.3f} bit. ".format(b))

info(0.9)
info(0.5)
info(0.1)