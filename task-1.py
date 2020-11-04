class Date:
    day = None
    month = None
    year = None

    def __init__(self, str_date):
        self.str_date = str_date
        Date.make_int(str_date)

    @classmethod
    def make_int(cls, str_date):
        try:
            lst_date = str_date.split('-')
            cls.day = int(lst_date[0])
            cls.month = int(lst_date[1])
            cls.year = int(lst_date[2])
        except ValueError as err:
            print(err)

    def __str__(self):
        Date.make_int(self.str_date)
        return f'{self.day}-{self.month}-{self.year}'

    @staticmethod
    def validate(date):
        try:
            if (0 < date.day <= 31) & (0 < date.month <= 12) & (0 < date.year <= 9999):
                print('Дата корректна')
            else:
                print("Дата некорректна")
        except TypeError as err:
            print(err)


d = Date('01-12-2020')
print(d)
d.validate(d)
