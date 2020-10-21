my_file = open("text_4.txt", encoding="utf-8")
file_content = my_file.readlines()
my_file.close()
eng_to_rus_dict = {"One": "один", "Two": "два", "Three": "три", "Four": "четыре"}

print(file_content)
new_file_content = ""
for line in file_content:
    for k in eng_to_rus_dict.keys():
        if line.find(k) >= 0:
            new_line = line.replace(k, eng_to_rus_dict.get(k))
            new_file_content += new_line
result_file = open("text_4_result.txt", "w", encoding="utf-8")
result_file.write(new_file_content)
result_file.close()
