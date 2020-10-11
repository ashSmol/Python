# Программа для работы со  списком товаров
print("*" * 30, "Меню", "*" * 30)
print("1 - добавить товар, 2 - вывести каталог товаров, 3 - вывести аналитику")
print("*" * 64)
goods = []
analytics = {}
user_input = ""
while user_input != "выход":
    user_input = input("введите номер команды или 'выход' чтобы выйти: ")
    print("_" * 100)
    if user_input == "1":
        product = input("Введите наименование товара: ")
        price = input("Введите цену товара: ")
        quantity = input("Введите количество товара: ")
        units = input("Введите единицы товара: ")
        record = {"наименование": product, "цена": price, "количество": quantity, "единицы": units}
        goods.append((len(goods), record))
        print("Вы ввели: ")
        print(record)
        print("_" * 100)
    elif user_input == "2":
        for product in goods:
            print(product)
        print("_" * 100)
    elif user_input == "3":
        products_list = []
        prices_list = []
        quantities_list = []
        units_list = []
        for product in goods:
            products_list.append(product[1].get("наименование"))
            prices_list.append(product[1].get("цена"))
            quantities_list.append(product[1].get("количество"))
            units_list.append(product[1].get("единицы"))
        analytics = {"наименования": products_list, "цены": prices_list, "количества": quantities_list,
                     "единицы": list(set(units_list))}
        for key in analytics.keys():
            print(f"{key} : {analytics.get(key)}")
        print("_" * 100)
        print("1 - добавить товар, 2 - вывести каталог товаров, 3 - вывести аналитику")
        print("_" * 100)
