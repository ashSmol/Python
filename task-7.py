def fact(n):
    if n == 0:
        return 1
    return fact(n - 1) * n


def fact_gen(n):
    for i in range(0, n + 1):
        yield fact(i)


n = int(input("Введите число, факториал которого хотите вычислить: "))
for index, el in enumerate(fact_gen(n)):
    print(f"факториал {index} равен {el}")
