s = input("Введите текст: ")

cleaned = ""
for ch in s:
    if ch != " ":
        cleaned += ch.lower()

if cleaned == "":
    print("Нет текста")
else:
    ok = True
    n = len(cleaned)
    for i in range(n // 2):
        if cleaned[i] != cleaned[n - 1 - i]:
            ok = False
            break
    if ok:
        print("Палиндром")
    else:
        print("Не палиндром")
