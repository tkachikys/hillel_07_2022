# Создать родительский класс auto, у которого есть атрибуты:
# brand, age, cоlor, mark и weight.
# А так же методы: move, birthday и stop.
# Методы move и stop выводят сообщение на экран «move» и «stop»,а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта.
class auto(object):
    brand = "BMW"
    age = 2
    color = "black"
    mark = "X5"
    weight = 2.4

    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1
        print(f"Возраст авто: {self.age}")


auto_1 = auto("volvo", 4, "CX60")
auto_1.birthday()

