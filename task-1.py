def division(dividend, divider):
    try:
        print(f"Результат операции = {(int(dividend) / int(divider)):.2f}")
    except ZeroDivisionError:
        print("Делить на 0 нельзя!")
    except ValueError:
        print("Необходимо ввести числа")


a = input("Введите делимое: ")
b = input("Введите делитель: ")

division(a, b)
