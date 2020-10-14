def my_func(x, y):
    """функция вычисляет значение выражения x в степени -y"""
    a = x
    for i in range(1, abs(y)):
        x *= a
    return 1 / x


try:
    x = float(input("введите действительное положительное число x "))
    y = int(input("введите целое отрицательное число y "))
    if (x > 0) & (y < 0):
        print(my_func(x, y))
    else:
        print("неверный ввод!")
except ValueError:
    print("Необходимо вводить числа!")
