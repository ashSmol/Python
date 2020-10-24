from random import randint


class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return ' '.join((self.name, self.color, 'Поехалa вперед'))

    def stop(self):
        return ' '.join((self.name, self.color, 'остановилась'))

    def turn(self):
        return ' '.join((self.name, self.color, 'повернула ' + ["влево", "вправо", "назад"][randint(0, 2)]))

    def show_speed(self):
        return f'едет со скоростью {self.speed}'

    def out(self):
        print(self.go())
        print(self.turn())
        print(self.show_speed())
        print(self.stop())
        if self.is_police:
            print("опаньки полиция!")
        print()


class TownCar(Car):

    def show_speed(self):
        return self.speed if self.speed <= 60 else f"Превышение!!! скорость = {self.speed} км\ч. Максимальная допустимая" \
                                                   f" скорость для этого класса авто 60 км\ч."


class WorkCar(Car):

    def show_speed(self):
        return self.speed if self.speed < 40 else f"Превышение!!! скорость = {self.speed} км\ч. Максимальная допустимая" \
                                                  f" скорость для этого класса авто 40 км\ч."


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


town_car = TownCar(70, 'белый', 'жигули', False)
town_car.out()
town_car = TownCar(60, 'белый', 'жигули', False)
town_car.out()

print('*' * 100)
work_car = WorkCar(100, 'синий', "трактор", False)
work_car.out()
work_car = WorkCar(30, 'синий', "трактор", False)
work_car.out()

print('*' * 100)
sport_car = SportCar(30, 'красный', "феррари", False)
sport_car.out()
sport_car = SportCar(300, 'красный', "феррари", False)
sport_car.out()

print('*' * 100)
police_car = PoliceCar(100, 'черный', "БМВ", True)
police_car.out()
police_car = PoliceCar(200, 'Синий', "Мерседес", True)
police_car.out()
