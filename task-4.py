from random import randint
# программа генерит список из 10 случайных чисел от 0 до 9. выбирает неповторяющиеся элементы списка
my_list = [randint(0, 9) for i in range(10)]
print(my_list)
my_list = [element for element in my_list if my_list.count(element) == 1]
print(my_list)
