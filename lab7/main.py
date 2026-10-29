from functions import sum_digits, average, normalize_text, select_numbers

num = int(input("Введите целое число: "))
print("Сумма цифр:", sum_digits(num))
print("-" * 20)

line = input("Введите строку чисел через пробел: ").strip()
if line:
    numbers = [int(x) for x in line.split()]
else:
    numbers = []

avg = average(numbers)
if avg is None:
    print("Среднее: Нет данных")
else:
    print(f"Среднее: {avg:.2f}")

threshold = int(input("Введите порог (целое неотрицательное): "))
selected = select_numbers(numbers, threshold)
print("Выбранные числа:", selected)
print("-" * 20)

text = input("Введите произвольный текст: ")
print("Нормализованный текст:", normalize_text(text))
