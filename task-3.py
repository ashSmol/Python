# Пользователь вводит число n. Программа вычислает сумму чисел n + nn +nnn

n = input("Введите число n: ")
nn = n + n
nnn = n + n + n
summa = int(n) + int(nn) + int(nnn)
print(f"Сумма чисел n + nn + nnn равна: {summa}")
