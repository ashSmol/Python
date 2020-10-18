from itertools import count, cycle
# Программа генерирует список задонной длины, состоящий из последовательности целыч чисел начиная с задонного числа.
# затем выводит эдементы списка 2 раза
list_length = int(input("Введите количестов элементов в списке: "))
start_num = int(input("Введите число, с которого список будет начинаться: "))
my_list = []
i = 0
count_iter = count(start_num)
while i < list_length:
    my_list.append(next(count_iter))
    i += 1
print(my_list)

cycle_iter = cycle(my_list)
i = 0
while i < len(my_list) * 2:
    print(next(cycle_iter), end=" ")
    i += 1
