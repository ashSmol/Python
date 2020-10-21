with open("text_3.txt", encoding="utf-8") as my_file:
    lines = my_file.readlines()
workers_salaries = {list_from_el[:-1].split()[0]: float(list_from_el[:-1].split()[1]) for list_from_el in lines}

print("Список сотрудников с окладом менее 20 тыс $:")
poors = [el[0] for el in workers_salaries.items() if el[1] < 20000]
print(poors)
print(f"Среднее значение зп: {sum(workers_salaries.values()) / len(workers_salaries)}$")
