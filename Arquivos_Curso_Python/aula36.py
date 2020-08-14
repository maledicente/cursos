import json

carros_json = '{"Marca":"Honda","Modelo":"HRV","Cor":"Prata"}'

carros = json.loads(carros_json)

for x in carros:
   print(type(x))

print("----------------")

for x in carros.values():
   print(type(x))

for k,v in carros.items():
   print("- "+ k,": " + v)

carros2 = {
             "Marca":"Honda",
             "Modelo":"HRV",
             "Cor":"Prata"
         }

carros_json2=json.dumps(carros2)

print(carros_json2)