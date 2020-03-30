import random

"""" principais metodos

random.randint(x, y) = pega um numero aletorio dentro de um range
random.choice(list) = escolhe aletorio um item de minha lista

"""

my_list = [1, 10, 35]

number = random.randint(0, 1000000)
print(number)

number2 = random.choice(my_list)
print(number2)