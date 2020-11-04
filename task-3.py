class NotNumberFormat(Exception):
    def __init__(self, err_text):
        self.err_text = err_text


user_input = None
my_list = []
print('Введите числа. Из введенных чисел будет сформирован список. Для окончания ввода введите "stop":\n')
while True:
    user_input = input()
    if user_input == 'stop':
        break
    try:
        if not user_input.isdigit():
            raise NotNumberFormat('Введенная строка не является числом!!!')
        element = int(user_input)
        my_list.append(element)
    except NotNumberFormat as err_text:
        print(err_text)

print(my_list)
