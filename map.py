def dobro(x):
	return x*2

lista = [1,2,3,4,5]

""""
	- executa funcao para cada item da lista
	- dois parametros, a funcao e a lista
	- sempre converter para list se quiser ver no print

"""

print(list(map(dobro, lista))) 
