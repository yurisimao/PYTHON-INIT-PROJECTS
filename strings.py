var_string1 = "Yuri "
var_string2 = "Simão"
concatenado = var_string1 + var_string2
my_string = "Yuri Jose Oliveira Simão"

print(concatenado)
print(len(concatenado)) #retorna o tamanho #return int
print(concatenado[3]) #pega a posicao da string #return string
print(concatenado[0:2]) #pega um inicio e um final da string #return string
print(concatenado.lower()) #low case
print(concatenado.upper()) #upper case
print(concatenado.strip()) #remove caracteres especiais ou espaços
print(my_string.split(" ")) #split pela string #return list
print(my_string.find("O")) #devolve a posicao que inicia a string #return int
print(my_string.replace("Yuri", "yuri")) #substitui uma string por outra