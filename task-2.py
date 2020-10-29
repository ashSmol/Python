from abc import ABC, abstractmethod


class Dress(ABC):
    @abstractmethod
    def calculate_material(self):
        pass


class Coat(Dress):
    def __init__(self, __v):
        self.__v = __v

    @property
    def calculate_material(self):
        return round(self.__v / 6.5 + 0.5, 2)


class Suit(Dress):
    def __init__(self, __h):
        self.__h = __h

    @property
    def calculate_material(self):
        return round(2 * self.__h + 0.3, 2)


coat = Coat(56)
print(coat.calculate_material)

suit = Suit(5)
print(suit.calculate_material)
