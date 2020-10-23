class Road:
    _length = 5000
    _width = 20

    def __init__(self):
        Road._length = int(input("Введите длину дорого: "))
        Road._width = int(input("Введите ширину дороги: "))

    def _calculate(self):
        return Road._length * Road._width * 25 * 5 / 1000


r1 = Road()
print(f"Для постройки такой дороги потребуется {r1._calculate()} тонн асфальта")
