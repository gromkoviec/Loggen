import json
import random
import logging

separator_path = input("Separators file location: ")
if separator_path == "":
    separator_path = "./configs/data_separators.jason"
else:
    separator_path = separator_path

logging.debug("Separators file uploaded")

#separator_path = "./configs/data_separators.jason"

with open(separator_path, "r") as fp:   # with open otwiera i zamyka plik
    sep_load = json.load(fp)

file_path = input("Data collected file location: ")
if file_path == "":
    file_path = "./configs/data_config2.jason"
else:
    file_path = file_path

   # "./configs/data_config2.jason" # TODO dopisac możliwośc z lini komend

logging.debug("Data collected file uploaded")
logging.debug("Login generator starts")

with open(file_path, "r") as fp:   # with open otwiera i zamyka plik
    dat_load = json.load(fp)

sep_list = list(sep_load.values())

print(sep_list)

imput_login_list = list(dat_load.values())

splited_imput_login_list = []

for x in imput_login_list:
    split_1 = x.split(" ")
    if len(split_1) != 1:
        splited_imput_login_list.extend(split_1)
    split_2 = x.split(".")
    if len(split_2) != 1:
        splited_imput_login_list.extend(split_2)
    split_3 = x.split("-")
    if len(split_3) != 1:
        splited_imput_login_list.extend(split_3)
    splited_imput_login_list.append(x)

#imput_separator_list = ["", "_", ".", "-"] # TODO wyrzucić do jsona

random_data = random.choice(imput_login_list)
random_data2 = random.choice(imput_login_list)
random_sign = random.choice(separator_path)
radom_login = random_data + random_sign + random_data2
print(random_data)

for x in splited_imput_login_list:
    for y in separator_path:
        for z in splited_imput_login_list:
            print(x+y+z)