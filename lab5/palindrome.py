s = input("Введите текст: ")

cleaned = ""
for ch in s:
    if ch != " ":
        cleaned += ch.lower()

if cleaned == "":
    print("Нет текста")
elif cleaned == cleaned[::-1]:
    print("Палиндром")
else:
    print("Не палиндром")
