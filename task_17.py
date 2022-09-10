# Прочитать сохранённый json-файл из задания №16 и записать данные на диск в csv-файл,
# первой строкой которого озаглавив каждый столбец и добавив новый столбец “телефон”.
import csv
import json
from random import randint


with open("friends.json") as f:
    output_dict = json.load(f)
    keys = output_dict.keys()
    value = output_dict.values()
    id_csv = list(keys)
    dic_csv = list(value)

name_lines = ["id", "name", "age", "phone"]
phone_number = []
x = 0
while True:
    if x < 6:
       phone_number.append(randint(0000000, 9999999))
       x += 1
    else:
       break

with open("friends_1.csv", mode="w", newline="", encoding="utf-8") as f:
    file_writer = csv.writer(f)
    file_writer.writerow(name_lines)
    for i, element in enumerate(id_csv):
        row_1 = id_csv[i], dic_csv[i][0], dic_csv[i][1], phone_number[i]
        file_writer.writerow(row_1)


