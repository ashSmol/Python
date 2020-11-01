class Warehouse:
    pass


class OfficeEquipment:
    def __init__(self, manufacturer, model):
        self.model = model
        self.manufacturer = manufacturer


class Printer(OfficeEquipment):
    def __init__(self, manufacturer, model, is_color):
        OfficeEquipment.__init__(self, manufacturer, model)
        self.is_color = is_color


class Scanner(OfficeEquipment):
    def __init__(self, manufacturer, model, is_manual):
        OfficeEquipment.__init__(self, manufacturer, model)
        self.is_manual = is_manual


class Copier(OfficeEquipment):
    def __init__(self, manufacturer, model, is_analog):
        OfficeEquipment.__init__(self, manufacturer, model)
        self.is_analog = is_analog
