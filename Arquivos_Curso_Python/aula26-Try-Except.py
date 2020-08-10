try:
  print(x)
except NameError:
  print("X não definido")
except:
  print("Erro desconhecido")

num =15
if not type(num) is int:
  raise Exception("Somente numeros")
else:
  print(num)