import time


class auto(object):
    brand = "Бренд авто"
    age = 0
    color = "Цвет авто"
    mark = "Марка авто"
    weight = "Вес авто"

    def __init__(self, brand, age, mark):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print(f"{self.brand} {self.mark} move")

    def stop(self):
        print(f"{self.brand} {self.mark} stop")

    def birthday(self):
        self.age += 1
        print(f"Возраст авто {self.brand} {self.mark} : {self.age}")


class truck(auto):
    max_load = None

    def __init__(self, brand, age, mark, max_load):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def move(self):
        print(f"attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("Load")
        time.sleep(1)


class car(auto):
    max_speed= 0

    def __init__(self, brand, age, mark, max_speed):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed {self.brand} {self.mark} is {self.max_speed}")


car_1 = car("Fiat", 10, "Punto", 160)
car_1.move()
car_1.stop()
print("-" * 20)
car_2 = car("Huyndai", 2, "Tucson", 200)
car_2.birthday()
print("-" * 20)
truck_1 = truck("Volvo", 10, "BIG", 20)
truck_1.move()
print("-" * 20)
truck_2 = truck("Man", 10, "racer", 20)
truck_2.load()
