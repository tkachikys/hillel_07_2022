import openpyxl
from Main_work_1 import data_person
while True:
    a = int(input("""Выберите действие: \n1.Ввести новые данные; 
2.Найти данные человека; \n3.Узнать возраст человека;\n4.Выйти из программы \nВаш выбор: """))
    if a == 1:
        a = int(input("   1.Записать новые данные; \n   2.Загрузить свой файл с данными?\n   3.Назад\n   Ваш выбор: "))
        if a == 1:
            data_person.write()
        elif a == 2:
            data_person.load_data()
        elif a == 3:
            continue
        else:
            print("Ошибочный ввод, выберите цифру с меню")
            continue
    elif a == 2:
        data_person.find_data()
        break
    elif a == 3:
        data_person.person_age()
        break
    elif a == 4:
        break
    else:
        print("Ошибочный ввод, выберите цифру с меню")
    #Меню работает, нужно сдлеть обработку исключений
