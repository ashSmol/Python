def user_data(**kwargs):
    print(kwargs)


user_data(name=input("Введите имя: "), surname=input("Введите фамилию: "), year_born=input("Введите год рождения: "),
          city=input("Введите город: "), email=input("Введите email: "), phone_num=input("Введите телефон: "))
