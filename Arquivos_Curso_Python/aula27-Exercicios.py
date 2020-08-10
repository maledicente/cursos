import os
import time
carros=[]
secs=5

class Carro:
  nome=""
  pot=0
  velMax=0
  ligado=False

  def __init__(self,nome,pot):
    self.nome=nome
    self.pot=pot
    self.velMax=int(pot)*2
    self.ligado=False

  def ligar(self):
    self.ligado=True

  def desligar(self):
    self.ligado=False

  def info(self):
    print("Nome..........:"+self.nome)
    print("Potencia......:"+self.pot)
    print("Vel. Maxima...:"+self.velMax)
    print("Estado:.......:"+("Sim" if self.ligado==True else "Não"))

def Menu():
  os.system("clear") or None
  print("1 - Novo Carro")
  print("2 - Informacoes do Carro")
  print("3 - Excluir Carro")
  print("4 - Ligar Carro")
  print("5 - Desligar Carro")
  print("6 - Listar Carros")
  print("7 - Sair")
  print("Quantidade de Carros: "+str(len(carros))+"\n")
  opc=input("Digite uma opcao: ")
  return opc

def NovoCarro():
  os.system("clear") or None
  n=input("Nome do Carro......: ")
  p=input("Potencia do Carro..:")
  car=(Carro(n,p))
  carros.append(car)
  print("Novo Carro criado com sucesso!")
  time.sleep(secs)

def informacoes():
  os.system("clear") or None
  n=input("Informe o numero do carro para consulta: ")
  try:
    carros[int(n)].info()
  except:
    print("Carro não existe na lista.")
  time.sleep(secs)

def excluirCarro():
  os.system("clear") or None
  n=input("Informe o numero do carro para excluir: ")
  try:
    del carros[int(n)]
  except:
    print("Carro não existe na lista.")

def ligarCarro():
  os.system("clear") or None
  n=input("Informe o numero do carro para ligar: ")
  try:
    carros[int(n)].ligar()
    print("Carro ligado")
  except:
    print("Carro não existe na lista.")

def desligarCarro():
  os.system("clear") or None
  n=input("Informe o numero do carro para desligar ")
  try:
    carros[int(n)].desligar()
    print("Carro ligado")
  except:
    print("Carro não existe na lista.")

def listarCarros():
  os.system("clear") or None
  p=0
  for c in carros:
    print(str(p)+" - "+c.nome)
    p=p+1
  time.sleep(secs)

ret=Menu()
while (ret < "7"):
  if   ret=="1": NovoCarro()
  elif ret=="2": informacoes()
  elif ret=="3": excluirCarro()
  elif ret=="4": ligarCarro()
  elif ret=="5": desligarCarro()
  elif ret=="6": listarCarros()
  ret=Menu()

os.system("clear")
print("Programa finalizando...") 
time.sleep(2)




