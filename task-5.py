def summ_str(string):
    summ = 0
    digits_list = string.split()
    for element in digits_list:
        if element.isdigit():
            summ += int(element)
    return summ


string = ""
total_sum = 0
while string.find("q") < 0:
    string = input("Введите числа через пробел. Для выхода введите 'q' \n")
    summ_string = summ_str(string)
    total_sum += summ_string
    print(f"сумма чисел в строке равна = {summ_string}. Общая сумма равна = {total_sum}")
