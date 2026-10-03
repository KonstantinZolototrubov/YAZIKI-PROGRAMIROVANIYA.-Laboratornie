n = int(input("Введите n: "))
count = 0
sum_val = 0

for i in range(n):
    x = int(input("Введите число: "))
    if x % 3 != 0:
        count += 1
        sum_val += x

print("Количество:", count)
print("Сумма:", sum_val)
