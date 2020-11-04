item_reference = {}


def register_item(item):
    item_reference[len(item_reference) + 1] = item


class Company:
    def __init__(self, depts_list):
        self.depts = {}
        for el in depts_list:
            self.depts.update({len(self.depts) + 1: el})

    def __str__(self):
        result = ''
        for el in self.depts:
            result += f'{el}. {self.depts.get(el).name}\n'
        return result


class NegativeAmountException(Exception):
    def __init__(self, err_text):
        self.err_text = err_text


class CompanyDepartment:
    def __init__(self, name):
        self.name = name
        self.items_quantities = {key_: 0 for key_ in item_reference.keys()}

    def __str__(self):
        result = ''
        for el in self.items_quantities:
            if self.items_quantities.get(el) > 0:
                result += f'{el}. {item_reference.get(el).__class__.__name__} {item_reference.get(el)} - ' \
                          f'{self.items_quantities[el]} шт \n'
        return result if result != '' else 'В отделе пока нет оборудования'

    @staticmethod
    def move_item(from_dep_1, to_dep_2, item_id, quantity=1):
        try:
            if from_dep_1.items_quantities[item_id] - quantity < 0:
                raise NegativeAmountException(f'Невозможно переместить оборудования больше чем есть в отделе')
            from_dep_1.items_quantities[item_id] = from_dep_1.items_quantities[item_id] - quantity
            to_dep_2.items_quantities[item_id] = to_dep_2.items_quantities[item_id] + quantity
        except NegativeAmountException as err:
            print(err)

    def get_equipment_by_type(self, equipment_type):

        result = f'{equipment_type}s:\n'
        for key_ in self.items_quantities:
            if (item_reference.get(key_).__class__.__name__ == equipment_type) & (self.items_quantities[key_] > 0):
                result += f'{item_reference[key_]} - {self.items_quantities[key_]} шт \n'
        return result if result != f'{equipment_type}s:\n' else f'В отделе {self.name} отсутсвет запрашиваемое оборудование'


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

depts_list = [counting_dept, h_r_dept, admin_dept, dev_dep, design_dep, wh]
equipment_dict = {}
equipment_dict = {1: 'Printer', 2: 'Scanner', 3: 'Copier'}
my_company = Company(depts_list)

CompanyDepartment.move_item(wh, h_r_dept, 4, 2)
print(equipment_dict)
# d = {}
# print({len(d) + 1: el for el in 'asdfg'})

# print(my_company.depts[int('2')].get_equipment_by_type(equipment_dict[equipment_dict]))


user_input = ''
while user_input != 'выход':
    print('*' * 50 + '   Меню   ' + '*' * 50)
    print('Выберите отдел предприятия. для выхода введите "выход"')
    print('*' * 110)
    print(my_company)
    user_input = input('Ваш выбор: ')
    if user_input == "выход":
        break
    else:
        dept = user_input
        command = ''
        while command != '3':
            print('*' * 50 + '   Меню   ' + '*' * 50)
            print(
                f'1. Вывод всего оборудования отдела {my_company.depts[int(dept)].name}. 2. Вывод оборудования по типу '
                f'3. Вернуться к выбору отдела')
            print('*' * 110)
            command = input("Ваш выбор: ")
            if command == '1':
                print(my_company.depts[int(dept)])
            if command == '2':
                equipment_type = ''
                while equipment_type != '4':
                    print('*' * 50 + '   Меню   ' + '*' * 50)
                    print('Выберите тип оборудования: ')
                    print('*' * 110)
                    for el in equipment_dict:
                        print(f'{el}. {equipment_dict[el]}')
                    print('4. Вернуться')
                    equipment_type = input('Введите номер желаемого типа оборудования: ')
                    if equipment_type == '4':
                        break
                    print(my_company.depts[int(dept)].get_equipment_by_type(equipment_dict[int(equipment_type)]))
