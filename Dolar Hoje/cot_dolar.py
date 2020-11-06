#Importando bibliotecas. 
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
import requests
import json

url = 'https://economia.awesomeapi.com.br/all/USD-BRL'
requisicao = requests.get(url)
cotacao = requisicao.json()

print('#### Cotação do Dolar ####')
print ('Moeda: ' + cotacao['USD']['name'])
print ('Data: ' + cotacao['USD']['create_date'])
print('Valor atual: R$' + cotacao['USD']['bid'])
