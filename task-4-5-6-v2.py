item_reference = {}


class Company:
    def __init__(self, depts_list):
        self.depts = {}
        for el in depts_list:
            self.depts.update({len(self.depts) + 1: el.name})

    def __str__(self):
        result = ''
        for el in self.depts:
            result += f'{el}. {self.depts.get(el)}\n'
        return result


class NegativeAmountException(Exception):
    def __init__(self, err_text):
        self.err_text = err_text


def register_item(item):
    item_reference[len(item_reference) + 1] = item


class CompanyDepartment:
    def __init__(self, name):
        self.name = name
        self.items_quantities = {key_: 0 for key_ in item_reference.keys()}

    def __str__(self):
        result = ''
        for el in self.items_quantities:
            if self.items_quantities.get(el) > 0:
                result += f'{el}. {item_reference.get(el).__class__.__name__} {item_reference.get(el)} - {self.items_quantities[el]} шт \n'
        return result

    @staticmethod
    def move_item(from_dep_1, to_dep_2, item_id, quantity=1):
        try:
            if from_dep_1.items_quantities[item_id] - quantity < 0:
                raise NegativeAmountException(f'Невозможно переместить оборудования больше чем есть в отделе')
            from_dep_1.items_quantities[item_id] = from_dep_1.items_quantities[item_id] - quantity
            to_dep_2.items_quantities[item_id] = to_dep_2.items_quantities[item_id] + quantity
        except NegativeAmountException as err:
            print(err)


class Warehouse(CompanyDepartment):
    def __init__(self):
        self.name = 'Склад'
        self.items_quantities = {key_: 5 for key_ in item_reference.keys()}


class OfficeEquipment:
    def __init__(self, manufacturer, model):
        self.model = model
        self.manufacturer = manufacturer

    def __str__(self):
        return f'{self.manufacturer} {self.model}'


class Printer(OfficeEquipment):
    def __init__(self, manufacturer, model, is_color):
        super().__init__(manufacturer, model)
        self.is_color = is_color


class Scanner(OfficeEquipment):
    def __init__(self, manufacturer, model, is_manual):
        super().__init__(manufacturer, model)
        self.is_manual = is_manual


class Copier(OfficeEquipment):
    def __init__(self, manufacturer, model, is_analog):
        super().__init__(manufacturer, model)
        self.is_analog = is_analog


register_item(Printer('hp', '3110', False))
register_item(Printer('epson', 'photo', True))
register_item(Printer('cannon', '10', False))
register_item(Printer('samsung', 'ML2010', False))
register_item(Printer('brother', '110', True))

register_item(Scanner('cannon', 'Lide11', False))
register_item(Scanner('epson', 'scan333', False))
register_item(Scanner('samsung', 'scan222', True))
register_item(Scanner('epson', 'scan111', False))
register_item(Scanner('brother', 'scan555', True))

register_item(Copier('cannon', 'L11', False))
register_item(Copier('HP', 'LaserJet Pro MFP M28a', False))
register_item(Copier('Xerox', 'WorkCentre 3025V_BI', True))
register_item(Copier('Pantum ', 'M6500', False))
register_item(Copier('brother', 'copier555', True))

counting_dept = CompanyDepartment('Бухгалтерия')
h_r_dept = CompanyDepartment('Отдел Кадров')
admin_dept = CompanyDepartment('Администрация')
dev_dep = CompanyDepartment('Разработка')
design_dep = CompanyDepartment('Дизайн')
wh = Warehouse()

depts_list = [counting_dept, h_r_dept, admin_dept, dev_dep, design_dep]


my_company = Company(depts_list)
user_command = ''

#d = {}
#print({len(d) + 1: el for el in 'asdfg'})

while user_command != 'выход':
    print('*' * 50 + '   Меню   ' + '*' * 50)
    print('введите номер оборудования для перемещения: ')
    item_id = input()
