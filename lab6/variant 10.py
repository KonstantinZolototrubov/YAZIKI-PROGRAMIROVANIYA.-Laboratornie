line = input("Введите числа: ").strip()

if not line:
    numbers = []
else:
    numbers = [int(x) for x in line.split()]

result = []
for num in numbers:
    if num >= 10:
        result.append(num)

count = len(result)
total = sum(result)
sorted_copy = sorted(result)

print("Список:", result)
print("Количество:", count)
print("Сумма:", total)
print("Отсортированный:", sorted_copy)
