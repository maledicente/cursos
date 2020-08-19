import pandas as pd 
#Cria um DataFrame
data = {'Empresa':['GOOGLE', 'GOOGLE', 'MSFT', 'MSFT','FB','FB'],'Nome':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],'Venda':[200,120,340,124,243,350]} 
df=pd.DataFrame(data)
group=df.groupby('Empresa')

print(group.describe())
