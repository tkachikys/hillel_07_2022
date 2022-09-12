
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
        return f"{self.brand} {self.mark} move"

    @staticmethod
    def notation():
        print("it`s class auto whith some staticmethod and classmethod")

    @staticmethod
    def stop():
        print("stop")

    @classmethod
    def years_of_birh(cls, years_old):
        birth = 2022 - years_old
        return birth

    @classmethod
    def auto_data(cls, data):
        brand, age, mark = data
        return cls(brand, age, mark)

    def birthday(self):
        self.age += 1
        print(f"Возраст авто: {self.age}")


user_auto = ["Fiat", 9, "Punto"]
user_auto_2 = ["Volvo", 3, "CX-90"]

auto_1 = auto.auto_data(user_auto)#Перевірка classmethod
auto_2 = auto.auto_data(user_auto_2)
print(auto_1.move())
print(auto_2.years_of_birh(auto_2.age))

auto.stop()#Перевірка staticmethod, як воно працює зрозумів але практичну користь поки що не знайшов
auto.notation()
