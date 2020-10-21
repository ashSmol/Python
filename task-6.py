def get_numbers_list(string):
    num = []
    for el in string.split():
        while not el.isdigit():
            if len(el) == 0:
                break
            el = el[0:-1:]
        if len(el) != 0:
            num.append(int(el))
    return num


with open("text_6.txt", "r", encoding="utf-8") as my_file:
    file_content = my_file.readlines()
my_dict = {}
for el in file_content:
    k = el[0: el.index(":"):]
    el = el[el.index(":") + 1::]
    get_numbers_list(el)
    my_dict.update({k: sum(get_numbers_list(el))})
print(my_dict)
