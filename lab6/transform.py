line = input("Введите числа: ").strip()
original = []

if line:
    original = [int(x) for x in line.split()]

new_list = []
for num in original:
    if num < 0:
        new_list.append(-num)
    else:
        new_list.append(num)

print("Исходный:", original)
print("Новый:", new_list)
