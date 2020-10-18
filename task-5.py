from functools import reduce


def proizvedenie(a, b):
    return a * b


my_list = [element for element in range(100, 1001) if element % 2 == 0]
print(reduce(proizvedenie, my_list))

