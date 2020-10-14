"""Программа отфильтровывает слова содержащие кирилицу и заглавные буквы. Выводит оставшиеся слова с заглавной буквы"""


def is_suitable(word):
    for letter in list(word):
        if ord(letter) not in range(97, 123):
            return False
    return True


my_string = input("Введите строку состоящую из нескольких слов, разделенных пробелами: \n")
words = my_string.split()
new_string = ''
for word in words:
    if is_suitable(word):
        new_string = new_string + word.title() + ' '
print(f"результат: {new_string}")
