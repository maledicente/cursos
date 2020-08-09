class Carro:
  velMax=0
  ligado=False
  cor=""
  def __init__(self,v,l,c):
    self.velMax=v
    self.ligado=l
    self.cor=c

  def mostrar(self):
    print("\nVelocidade maxima: "+str(self.velMax))
    print("Cor..............: "+self.cor)
    estado="Sim" if self.ligado else "Não"
    print("Ligado...........: "+estado)
    print("-------The end-------\n")
  
  def ligar(self):
    self.ligado=True

  def desligar(self):
    self.ligado=True
  
  def andar(self):
    if(self.ligado):
      print("Andando")
    else:
      print("Carro desligado")


c1=Carro(200,False,"Preto")
c1.mostrar()
c1.ligar()
c1.mostrar()

