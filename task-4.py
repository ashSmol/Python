# ПРограмма находит и выводит самую большую цифру во введенном числе
n = int(input("Введите число целое положительное число: "))
max_digit = 0
while n != 0:
    last_digit = n % 10
    if last_digit > max_digit:
        max_digit = last_digit
    n = n // 10
print("самая большая цифра во введенном числе: ", max_digit)
