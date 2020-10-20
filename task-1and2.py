with open("my_text.txt", mode="a+", encoding="utf-8") as my_file:
    user_line = " "
    while True:
        user_line = input("Введите строку для добавления в файл.\nДля выхода введите пустую строку:\n")
        if user_line == "":
            break
        print(user_line, file=my_file)
    my_file.seek(0)
    strs_list = my_file.readlines()
    my_file.seek(0)
    print("Содержимое файла:")
    print(my_file.read())
    print(f"Количество строк в файле равно: {len(strs_list)}")

    for index, el in enumerate([len(stroka.split()) for stroka in strs_list]):
        print(f"Количество слов в строке №{index + 1} равно: {el}")
