# Программа меняет местами пары элементов 0 -> 1, 2 -> 3 и тд
my_list = input("Введите элементы списка через ',': ")
my_list = my_list.split(",")

for i in range(1, len(my_list), 2):
    my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]
print(my_list)
