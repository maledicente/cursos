class Carro:
  velMax=0
  ligado=False
  cor=""

c1=Carro()
c2=Carro()
c3=Carro()

c1.velMax=200
c1.cor="Preto"
c1.ligado=False

print("\nValocidade maxima: "+str(c1.velMax))
print("Cor: "+c1.cor)
estado="Sim\n" if c1.ligado else "Não\n"
print("Ligado: "+estado)