from random import randint

my_str = ""
with open("my_file.txt", "w", encoding="utf-8") as my_file:
    for _ in range(10):
        my_str += str(randint(0, 9)) + ' '
    my_file.write(my_str)

with open("my_file.txt", "r", encoding="utf-8") as my_file:
    file_content = my_file.read()
print(f"Содержимое сгенеренного файла: \n {file_content}")
print(f"Сумма чисел из файла равна: {sum(int(el) for el in file_content.split())}")
