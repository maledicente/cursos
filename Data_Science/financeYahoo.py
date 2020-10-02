## Álgebra Linear
import numpy as np

## Leitura de Dados da Web
from pandas_datareader import data as wb 

## Plots
import matplotlib.pyplot as plt

## Ativos da Amazon desde 01/01/2000 
AMZN = wb.DataReader('AMZN', data_source='yahoo', start ='2000-01-01')

## Conferindo o cabeçalho
AMZN.head()

## Conferindo o final do cabeçalho
AMZN.tail()

## Dividindo o número de fechamento pelo dia de fechamento do dia anterior com o uso do shift.
AMZN['simple_return'] = (AMZN['Adj Close'] / AMZN['Adj Close'].shift(1)) - 1
print (AMZN['simple_return'])

## Plotando a taxa de retorno simples
AMZN['simple_return'].plot(figsize=(8,5))
plt.show()

## Retorno médio diário ao longo do tempo
retorno_medio_diario = AMZN['simple_return'].mean() * 250
print(round(retorno_medio_diario,5) * 100)

## Criando nova coluna com os valores de log return
AMZN['log_return'] = np.log(AMZN['Adj Close']/AMZN['Adj Close'].shift(1))

## Calculando o retorno médio diário ao longo do tempo
retorno_medio_diario = AMZN['log_return'].mean() * 250
print(round(retorno_medio_diario, 5) * 100)

## Álgebra Linear
import numpy as np

## Manipulação dos Dados
import pandas as pd

## Webscraping do Yahoo Finance
from pandas_datareader import data as wb

## Visualizações
import matplotlib.pyplot as plt

## Amazon, Microsoft e Ford
tickers = ['AMZN','MSFT', 'F']

## Criando o df
carteira = pd.DataFrame()

## Extraindo os dados de fechamento
for t in tickers:
    carteira[t] = wb.DataReader(t, data_source='yahoo', start='2000-1-1')['Adj Close']

(carteira / carteira.iloc[0] * 100).plot(figsize = (15,6));
plt.show()

## Taxa de Retorno Simples
TR = (carteira / carteira.shift(1)) - 1
## Pesos de cada ativo
pesos = np.array([0.35, 0.35, 0.30])
## Retorno médio ao longo do ano (tirando os finais de semana)
retorno_anual = TR.mean() * 250
## TRC (calculando e printando)
TRC = (round(np.dot(retorno_anual, pesos),5)*100)
print (TRC)

## Álgebra Linear
import numpy as np

## Manipulação dos Dados
import pandas as pd

## Webscraping do Yahoo Finance
from pandas_datareader import data as wb

## Amazon e Mercado
tickers = ['AMZN', '^GSPC']

## Criando o Df
data = pd.DataFrame()

## Coletando os dados do Yahoo Finance no período estipulado (dados de fechamento)
for t in tickers:
    data[t] = wb.DataReader(t, data_source='yahoo', start='2014-1-1', end='2019-12-31')['Adj Close']

## Utilizando o retorno logarítmico (em relação as ações)
retorno_log = np.log( data / data.shift(1) )

## Calculando a Covariância (desconsiderando os finais de semana)
cov = retorno_log.cov() * 250
print(cov)

## Covariância AMZN em relação ao mercado (linha 0 e coluna 1)
Covariancia_Mercado = cov.iloc[0,1]

## Variância do mercado (desconsiderando os finais de semana)
Variancia_Mercado = retorno_log['^GSPC'].var() * 250

## Calculando o Beta da AMZN
AMZN_beta = Covariancia_Mercado/ Variancia_Mercado
print(AMZN_beta)

## CAPM
AMZN_capm = 0.0069 + AMZN_beta * 0.05
print(AMZN_capm)

## Índice SHARPE
Sharpe = (AMZN_capm - 0.0069) / (retorno_log['AMZN'].std() * 250 ** 0.5)
print(Sharpe)

