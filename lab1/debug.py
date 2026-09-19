print("=== Фрагмент А ===")
first = "2"
second = "3"
print("Типы до:", type(first), type(second))
first = int(first)
second = int(second)
print("Типы после:", type(first), type(second))
print("Результат А:", first + second)

print("\n=== Фрагмент Б ===")
age = input("Возраст: ")
print("Тип до:", type(age))
age = int(age)
print("Тип после:", type(age))
print("Результат Б:", age + 1)

print("\n=== Фрагмент В ===")
first = 4
second = 7
third = 10
average = (first + second + third) / 3
print("Результат В:", average)

print("\n=== Проверка с другими значениями ===")
first = "10"
second = "20"
print("А (10+20):", int(first) + int(second))
age = 25
print("Б (25+1):", age + 1)
first = 2
second = 3
third = 6
average = (first + second + third) / 3
print("В ((2+3+6)/3):", average)
