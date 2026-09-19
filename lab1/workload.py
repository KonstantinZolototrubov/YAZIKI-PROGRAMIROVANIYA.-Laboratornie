sub1 = input("Название первого предмета: ")
count1 = int(input("Количество занятий: "))
dur1 = int(input("Длительность занятия (мин): "))

sub2 = input("Название второго предмета: ")
count2 = int(input("Количество занятий: "))
dur2 = int(input("Длительность занятия (мин): "))

min1 = count1 * dur1
min2 = count2 * dur2
total_min = min1 + min2
total_hours = total_min / 60

avail = float(input("Доступное время на неделю (ч): "))

free = avail - total_hours
four_weeks = total_hours * 4

print("\n" + sub1 + ": " + str(min1) + " мин.")
print(sub2 + ": " + str(min2) + " мин.")
print("Общая нагрузка: " + str(total_min) + " мин. или {:.2f} ч.".format(total_hours))
print("Остаток свободного времени: {:.2f} ч.".format(free))
print("Нагрузка за 4 недели: {:.2f} ч.".format(four_weeks))
