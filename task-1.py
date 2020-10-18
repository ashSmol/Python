from sys import argv

name, work_hours, hour_price, bonus = argv
try:
    print(f"заработок составляет: {int(work_hours) * int(hour_price) + int(bonus)}")
except ValueError:
    print("необходимо ввести числовые значения!!!")
