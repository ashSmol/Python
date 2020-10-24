class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {}

    def __init__(self, name, surname, position, wages, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income.update({"wages": wages, "bonus": bonus})


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return Position._income.get('wages') + Position._income.get('bonus')


position = Position("Ivan", "Ivanov", "postman", 10000, 1000)
print(position.get_full_name())
print(position.get_total_income())
