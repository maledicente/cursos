import os

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
		  'N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for letra in letras:
	os.system(f'mkdir {letra}')
print('Foram criadas {} pastas.'.format(len(letras)))