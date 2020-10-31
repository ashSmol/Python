class Date:
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def make_int(cls, str_date):
        day = str_date.split('-')[0]
        month = str_date.split('-')[1]
        year = str_date.split('-')[2]
        return int(day), int(month), int(year)

    def __str__(self):
        return self.str_date

    @staticmethod
    def validate(day, month, year):
        if (0 < day <= 31) & (0 < month <= 12) & (0 < year <= 9999):
            print('Дата корректна')
        else:
            print("Дата некорректна")


d = Date('11-12-2020')
print(d)
print(Date.make_int('11-12-2200'))
d.validate(*Date.make_int('11-12-2200'))
