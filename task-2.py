class Road:
    _length = 5000
    _width = 20

    def __init__(self):
        self._length = int(input("Введите длину дороги в метрах: "))
        self._width = int(input("Введите ширину дороги в метрах: "))

    def calculate(self):
        return self._length * Road._width * 25 * 5 / 1000


r1 = Road()
print(f"Для постройки такой дороги потребуется {r1.calculate()} тонн асфальта")
