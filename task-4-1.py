def my_func(x, y):
    """функция вычисляет значение выражения x в степени -y"""
    return x ** y


try:
    x = float(input("введите действительное положительное число x "))
    y = int(input("введите целое отрицательное число y "))
    if (x > 0) & (y < 0):
        print(my_func(x, y))
    else:
        print("неверный ввод!")
except ValueError:
    print("Необходимо вводить числа!")
