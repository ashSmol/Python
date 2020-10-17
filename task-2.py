from random import randint

my_list = [randint(0, 100) for i in range(10)]
print(f"список сгенерированный случайным образом: {my_list}")
my_list = [my_list[element] for element in range(1, len(my_list)) if my_list[element - 1] < my_list[element]]
print(f"элементы списка выбраны из первого списка, если предыдущий элемент меньше последующего: {my_list}")

