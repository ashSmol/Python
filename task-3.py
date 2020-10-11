# Программа выводит название месяца по номеру, введенному пользователем
print("*" * 50)
print("решение задачи через кортеж")
print("*" * 50)
months_tuple = (
    "январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь")
month_nums = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
month_num = input("Введите номер месяца(число от 1 до 12): ")
while month_num not in month_nums:
    month_num = input("Введите номер месяца(число от 1 до 12): ")
month_num = int(month_num) - 1
print(f"Вы ввели номерь месяца - {months_tuple[month_num]}")
print()
print("*" * 50)
print("решение задачи через словарь")
print("*" * 50)
months_dict = {
    '1': "январь", '2': "февраль", '3': "март", '4': "апрель", '5': "май", '6': "июнь", '7': "июль", '8': "август",
    '9': "сентябрь", '10': "октябрь", '11': "ноябрь", '12': "декабрь"}

month_num = input("Введите номер месяца(число от 1 до 12): ")
while month_num not in month_nums:
    month_num = input("Введите номер месяца(число от 1 до 12): ")
print(f"Вы ввели номерь месяца - {months_dict[month_num]}")