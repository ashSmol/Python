# Программа вствляет введенное пользователем число в упорядоченный список
my_list = [8, 7, 5, 3, 3, 2]
print(my_list)
element = input("Введите число от 0 до 9: ")
while not element.isdigit():
    element = input("Введите число или 'exit' чтобы выйти: ")
for index in range(len(my_list), 0, - 1):
    if my_list[index - 1] >= int(element):
        my_list.insert(index, float(element))
        break
if max(my_list) < float(element):
    my_list.insert(0, float(element))
print(my_list)
