""""
	principais metodos do list

len(list) = retorna da tamanho da lista
list[posicao] = retorna o item da lista naquela posicao
list.append("item") = adiciona um item na lista
del list[init:end] = remove os items da lista passando um inicio e o fim para ela
list.sort() = rever do menor para o maior (int/ float) | ordem alfabética (string) / void altera a propria lista
sorted(list) = ordena do menor para o maior / retorna outra objeto do tipo lista
list.sort(reverse=True) = rever do maior para o menor (int/ float) | ordem alfabética inversamente (string) 
list.reverse() = ira reverter os itens da lista

"""

fruit_list = ["banana", "pera", "morango"]
number_list = [1283,223,2,432,55, 0]
estranged_list = [1.2, "item", True, False, 5]

print(len(fruit_list))

fruit_list.append("melancia")

if "acabate" in fruit_list:
	print("tem acabate")
else:
	print("nao tem acabate")		

fruit_list.sort()

print(fruit_list)