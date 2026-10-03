attempts = 0

while True:
    x = int(input("Введите целое число: "))
    if x > 0:
        break
    attempts +=1

print("Квадрат:", x * x)
print("Отклонено раз:",attempts)
