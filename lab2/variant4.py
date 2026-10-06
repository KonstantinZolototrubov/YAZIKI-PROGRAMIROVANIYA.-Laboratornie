total = int(input("Общий объём (количество деталей): "))
capacity = int(input("Вместимость одной единицы (деталей в контейнере): "))

full = total // capacity
remainder = total % capacity
total_units = (total + capacity - 1) // capacity

print("Полных единиц:", full)
print("Остаток:", remainder)
print("Всего единиц:", total_units)
