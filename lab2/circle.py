import math

r = float(input("Введите положительный радиус: "))

circumference = 2 * math.pi * r
area = math.pi * r * r

print(f"Длина окружности: {circumference:.2f}")
print(f"Площадь круга: {area:.2f}")
