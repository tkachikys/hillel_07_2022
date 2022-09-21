import openpyxl
import pandas as pd
from datetime import datetime, time, date


class data_person(object):
        @staticmethod
        def write():#Запись в хл файл
            r = sheet.max_row
            cell = sheet.cell(row=r + 1, column=1)
            cell.value = input("Введите имя: ")
            cell = sheet.cell(row=r + 1, column=2)
            cell.value = input("Введите фамилию: ")# не обязательно
            cell = sheet.cell(row=r + 1, column=3)
            cell.value = input("Введите отчество: ")# не обязательно
            cell = sheet.cell(row=r + 1, column=4)
            cell.value = input("Введите дату рождения(ДД-ММ-ГГ): ")
            cell = sheet.cell(row=r + 1, column=5)
            cell.value = input("Введите дату смерти(ДД-ММ-ГГ): ")# не обязательно
            cell = sheet.cell(row=r + 1, column=6)
            cell.value = input("Введите пол(М/Ж): ")
            wb.save("Test.xlsx")

        @staticmethod
        def load_data():#Загрузка файла в хл, не работает ДОДЕЛАЙ!
            a = input("Введите назваие файла: ")
            data_for_load = pd.read_excel(a,sheet_name="Sheet")
            writer = pd.ExcelWriter("Test.xlsx")
            data_for_load.to_excel(writer)
            writer.save()
            print("Напиши код загрузки файла")

        @staticmethod
        def find_data():#Поиск в файле, работает, нужно сделать независимость от регистра.
            text = input("   Введите имя для поиска: ")
            persons = pd.read_excel("Test.xlsx", sheet_name="Sheet")
            filter_person = persons["name"].str.contains(text)
            filter_person_1 = persons["surname"].str.contains(text)
            filter_person_2 = persons["second_name"].str.contains(text)
            print(persons.loc[filter_person | filter_person_1 | filter_person_2])
            print("Нужно сделать не зависимость от регистра, обработать ошибки")

        @staticmethod
        def person_age():#Вычисление возраста, работает, пока что только для живых людей
            df = pd.DataFrame
            text = input("   Введите имя для поиска: ")
            persons = pd.read_excel("Test.xlsx", sheet_name="Sheet")
            filter_person = persons["name"].str.contains(text)
            filter_person_1 = persons["surname"].str.contains(text)
            filter_person_2 = persons["second_name"].str.contains(text)
            person_to_age = persons.loc[filter_person | filter_person_1 | filter_person_2]
            birthday_person = person_to_age["birthday"]
            birthday_person_str = birthday_person.to_string()
            birthday_p_dt = datetime.strptime(birthday_person_str[-10:], "%d-%m-%Y")
            age_person = datetime.now().year - birthday_p_dt.year
            today = date.today()

            def age(age_person):
                if today.month < birthday_p_dt.month:
                    age_person -= 1
                elif today.month == birthday_p_dt.month and today.day < birthday_p_dt.day:
                    age_person -= 1
                return age_person

            print(age(age_person))


wb = openpyxl.Workbook()
sheet = wb["Sheet"]
name_colums = ["name", "surname", "second_name", "birthday", "dieday", "sex"]

for i in range(0, 6):
    cell = sheet.cell(row=1, column=i+1)
    cell.value = name_colums[i]

wb.save("Test.xlsx")
