# Создать программу-калькулятор в виде класса и несколько методов,
# как минимум сложение, вычитание, деление, умножение, возведение в степень и извлечение квадратного корня.
# Обернуть каждый метод в блок try/except и сделать обработку нескольких исключений, как минимум деление на 0.
# Создать своё исключение, к примеру возведение в отрицательную степень.
import math

class Calculator():

    def summa(self, x, y):
        try:
            result = int(x) + int(y)
            return print(result)
        except ValueError:
            print("Your input is not a number, try again")

    def sub(self, x, y):
        try:
            result = int(x) - int(y)
            return print(result)
        except ValueError:
            print("Your input is not a number, try again")

    def mult(self, x, y):
        try:
            result = int(x) * int(y)
            return print(result)
        except ValueError:
            print("Your input is not a number, try again")

    def devision(self, x, y):
        try:
            result = int(x) / int(y)
            return print(result)
        except ValueError:
            print("Your input is not a number, try again")
        except ZeroDivisionError:
            print("Can't divide by 0")

    def exponentiation(self, x, y):
        try:
            if int(y) < 0:
                raise ZeroDivisionError("Please enter a positive number")
            result = int(x) ** int(y)
            return print(result)
        except ValueError:
            print("Your input is not a number, try again")
        except ZeroDivisionError as err:
            print(err)
    def square(self, x):
        try:
            result = math.sqrt(int(x))
            return print(result)
        except ValueError:
            print("Your input is not a number, try again")


c = Calculator()


while True:
    try:
        choice = int(input("""Select an action: \n1. add\n2. subtraction\n3. multiplication
4. devision\n5. exponentiation\n6. root squaring\n7. exit\nYour choice: """))
        if choice == 7:
            break
        else:
            if choice == 1:
                x = input("Enter the first number: ")
                y = input("Enter the second number: ")
                c.summa(x, y)
            elif choice == 2:
                x = input("Enter the first number: ")
                y = input("Enter the second number: ")
                c.sub(x, y)
            elif choice == 3:
                x = input("Enter the first number: ")
                y = input("Enter the second number: ")
                c.mult(x, y)
            elif choice == 4:
                x = input("Enter the first number: ")
                y = input("Enter the second number: ")
                c.devision(x, y)
            elif choice == 5:
                x = input("Enter the first number: ")
                y = input("Enter the second number: ")
                c.exponentiation(x, y)
            elif choice == 6:
                x = input("Enter number: ")
                c.square(x)
    except ValueError:
        print("Your input is not a number, try again")








