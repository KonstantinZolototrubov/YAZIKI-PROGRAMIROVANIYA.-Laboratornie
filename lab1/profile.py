surname = input("Введите фамилию: ")
name = input("Введите имя: ")
group = input("Введите группу: ")
city = input("Введите город: ")
age = int(input("Введите возраст: "))
subject = input("Введите любимый предмет: ")
hours = float(input("Введите часы подготовки в неделю: "))

full_name = name + " " + surname
age_future = age + 4
hours_4_weeks = hours * 4
hours_day = hours / 7

print("\n" + "=" * 30)
print("КАРТОЧКА СТУДЕНТА")
print("=" * 30)
print("Полное имя:", full_name)
print("Группа:", group)
print("Город:", city)
print("Любимый предмет:", subject)
print("Возраст через 4 года:", age_future)
print("Время за 4 недели: {:.2f} ч.".format(hours_4_weeks))
print("Среднее время в день: {:.2f} ч.".format(hours_day))
print("=" * 30)
