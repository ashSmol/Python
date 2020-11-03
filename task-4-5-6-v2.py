item_reference = {}


class NegativeAmountException(Exception):
    def __init__(self, err_text):
        self.err_text = err_text


def register_item(item):
    item_reference[len(item_reference)] = item


def move_item(from_dep_1, to_dep_2, item_id, quantity=1):
    try:
        if from_dep_1.items_quantities[item_id] - quantity < 0:
            raise NegativeAmountException(f'Невозможно переместить оборудования больше чем есть в отделе')
        from_dep_1.items_quantities[item_id] = from_dep_1.items_quantities[item_id] - quantity
        to_dep_2.items_quantities[item_id] = to_dep_2.items_quantities[item_id] + quantity
    except NegativeAmountException as err:
        print(err)


class CompanyDepartment:
    def __init__(self):
        self.items_quantities = {key_: 0 for key_ in item_reference.keys()}

    def __str__(self):
        result = ''
        for el in self.items_quantities:
            if self.items_quantities.get(el) > 0:
                result += f'{item_reference.get(el)} - {self.items_quantities[el]} шт \n'
        return result


class Warehouse(CompanyDepartment):
    def __init__(self):
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

dep_1 = CompanyDepartment()
dep_2 = CompanyDepartment()
wh = Warehouse()

move_item(wh, dep_1, 5, 3)
move_item(wh, dep_1, 6, 4)

move_item(dep_1, dep_2, 5)

print(dep_2)
