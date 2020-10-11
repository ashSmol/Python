# Программа выводит первые 10 символов слов из введенной строки по номерам
my_list = input("Введите строку из нескольких слов разделенных пробелами: ").split()
for index, element in enumerate(my_list, 1):
    print(f"{index}. {element:.10}")
