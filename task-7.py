import json

with open("text_7.txt", "r", encoding="utf-8") as my_file:
    file_content = my_file.readlines()
my_dict = {}
total_profit = 0
profitable_count = 0
for el in file_content:
    my_list = el.split()
    profit = int(my_list[2]) - int(my_list[3])
    my_dict.update({my_list[0]: profit})
    if profit > 0:
        profitable_count += 1
        total_profit += profit

    avg_dict = {"average profit": total_profit / profitable_count}
list_for_json = [my_dict, avg_dict]

with open("text_777.json", "w") as json_file:
    json.dump(list_for_json, json_file, ensure_ascii=False, indent=4)
