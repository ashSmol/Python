# Программа вычисляет прибыльность/убытычность фирмы. в случае прибыльности рассчитывается прибыл на каждого сотрудника
# фирмы
gains = int(input("Введите полученную выручку: "))
losses = int(input("Введите понесенные убытки: "))
print()
if (gains - losses) > 0:
    print("Компания прибыльна")
    profit = gains - losses
    print(f"доход составил: {profit}")
    cost_effectiveness = profit / gains
    print(f"рентабельность выручки: {cost_effectiveness:.2f}")
    personal_count = int(input("Введите количество сотрудников: "))
    print(f"прибыль на человека составила: {(profit / personal_count):.2f}")
elif gains == losses:
    print("Компания не понесла убытков, но и не заработала!")
else:
    print("Компания убыточна")
