"""
		pricipais metodos do dicionario

my_map["CHAVE"] = retorna o valor
my_map.items() = retorna os itens do dicionario (chave e valor)
my_map.values() = retorna somentes os valores do dicionario
my_map.keys() = retorna as chaves do dicionario

"""

my_map = {"A": "Ameixa", "B":"Bola", "C" : "Cachorro"}

for key in my_map:
	print(key + " : " + my_map[key])

for x in my_map.values():
	print(x)

for y in my_map.keys():
	print(y)

for z in my_map.items():
	print(z)	


