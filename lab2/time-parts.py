total_seconds = int(input("Введите total_seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(hours, "ч", minutes, "мин", seconds, "с")
