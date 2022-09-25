# Создать генератор геометрической прогрессии
def geometric_generator(x, y):
    for i in range(x):
        yield y**i
        i += 1


x = int(input("Input range of progression: "))
y = int(input("Input value of progression: "))


finish_progression = []
for item in geometric_generator(x, y):
    finish_progression.append(item)

print(finish_progression)

