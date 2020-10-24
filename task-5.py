class Stationary:
    title = ""

    def draw(self):
        pass

    def __init__(self, title):
        self.title = title


class Pencil(Stationary):
    def draw(self):
        print(f"{self.title} рисует")


class Pen(Stationary):
    def draw(self):
        print(f"{self.title} пишет")


class Marker(Stationary):
    def draw(self):
        print(f"{self.title} выделяет")

pencil = Pencil("простой карандаш")
pencil.draw()
print("*" * 100)
pen = Pen("шариковая ручка")
pen.draw()
print("*" * 100)
marker = Marker("толсый маркер")
marker.draw()