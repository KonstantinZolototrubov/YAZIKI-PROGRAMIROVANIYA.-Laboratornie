n = int(input("Введите n: "))
x = int(input("Введите число: "))

total = x
positive = 1 if x > 0 else 0
max_val = x

for i in range(1, n):
        x = int(input("Введите число: "))
        total += x
        if x > 0:
            positive += 1
        if x > max_val:
            max_val = x

print("Сумма:",total)
print("Положительных:",positive)
print("Максимум:",max_val)                
