
class String(str):

     def __add__(self, other):
        x = str(self) + str(other)
        return String(x)

     def __sub__(self, other):
         x = str(self)
         y = str(other)
         new_string = x.replace(y, "", 1)
         return new_string


print(String("New") + String(890))
print(String("New") + 568)
print(String('New') + 'castle')
print(String('New') + 77)
print(String('New') + True)
print(String('New') + ['s', ' ', 23])
print(String('New') + None)

print(String('New bala7nce') - 7)
print(String('New balance') - 'bal')
print(String('New balance') - 'Bal')
print(String('pineapple apple pine') - 'apple')
print(String('New balance') - 'apple')
print(String('NoneType') - None)
print(String(55678345672) - 7)
