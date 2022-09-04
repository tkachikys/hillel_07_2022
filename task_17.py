# Прочитать сохранённый json-файл из задания №16 и записать данные на диск в csv-файл,
# первой строкой которого озаглавив каждый столбец и добавив новый столбец “телефон”.
import csv
import json

with open("Hillel_07_2022/friends.json") as f:
    output_dict = json.load(f)

name_lines = ["id", "name", "age", "phone"]
n = ["123", "123", "123", "123", "123", "123"]
t = list(output_dict.items())

with open("Hillel_07_2022/fiends_1.csv", mode="w", newline="", encoding="utf-8") as f:
    file_writer = csv.writer(f)
    file_writer.writerow(name_lines)
    for i in t:
        file_writer.writerow(i)


a =asfd


