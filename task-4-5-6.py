class Warehouse:
    def __init__(self):
        self.printers = {}
        self.scanners = {}
        self.copiers = {}

    def add_equipment(self, equipment):
        if type(equipment) == Printer:
            self.printers.update({max(self.printers.keys() if len(self.printers.keys()) != 0 else [0]) + 1: equipment})
        if type(equipment) == Scanner:
            self.scanners.update({max(self.scanners.keys() if len(self.scanners.keys()) != 0 else [0]) + 1: equipment})
        if type(equipment) == Copier:
            self.copiers.update({max(self.copiers.keys() if len(self.copiers.keys()) != 0 else [0]) + 1: equipment})

    def __str__(self):
        result = f'Printers:\n'
        for el in self.printers:
            result += f'{el}. {self.printers.get(el)}\n'
        result += f'Scanners:\n'
        for el in self.scanners:
            result += f'{el}. {self.scanners.get(el)}\n'
        result += f'Copiers:\n'
        for el in self.copiers:
            result += f'{el}. {self.copiers.get(el)}\n'
        return result


class OfficeEquipment:
    def __init__(self, manufacturer, model):
        self.model = model
        self.manufacturer = manufacturer

    def __str__(self):
        return f'Manufacturer: {self.manufacturer}, Model: {self.model}'


class Printer(OfficeEquipment):
    def __init__(self, manufacturer, model, is_color):
        super().__init__(manufacturer, model)
        self.is_color = is_color

    def __str__(self):
        return super.__str__(self) + f' Color: {self.is_color}'


class Scanner(OfficeEquipment):
    def __init__(self, manufacturer, model, is_manual):
        super().__init__(manufacturer, model)
        self.is_manual = is_manual


class Copier(OfficeEquipment):
    def __init__(self, manufacturer, model, is_analog):
        super().__init__(manufacturer, model)
        self.is_analog = is_analog


pr_1 = Printer('hp', '3110', False)
pr_2 = Printer('hp1', '3112', True)
sc_1 = Scanner('canon', '30', True)
cop = Copier('epson', '222', False)

sklad = Warehouse()
sklad.add_equipment(pr_1)
sklad.add_equipment(pr_2)
sklad.add_equipment(sc_1)
sklad.add_equipment(cop)
print(sklad)
print(pr_1)
