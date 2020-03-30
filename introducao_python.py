#Variables example
x = 3 #int
y = 2.3 #float
z = "I m String"
a = True
b = False
lista1= [1,2,3,4,5]
lista2 = ["ola", "mundo"]
lista3 = [0, "string", 1.3, True, False] #Item lista nao é tipado

#If example
if x == y:
	print("sao iguais")
elif x > y:
	print ("x e maior que y")
else:
	print("numeros diferentes")		


#while example
while x <= 10:
	print(x)
	x += 1

#foreach example
for i in lista1:
	print(i)

for i2 in lista2:
	print(i2)

for i3 in lista3:
	print(i3)

for i4 in range(10, 20, 2): #do primeiro item ate o segundo contando do terceiro item
	print(i4)			