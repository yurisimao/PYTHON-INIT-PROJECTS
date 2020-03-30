def pares(x):
	if x % 2 == 0:
		return x

lista = [1,2,3,4,5,6,7,8,9,10]

lista_pares = filter(pares, lista) # dois parametros, o metodo e o obj

print(list(lista_pares))