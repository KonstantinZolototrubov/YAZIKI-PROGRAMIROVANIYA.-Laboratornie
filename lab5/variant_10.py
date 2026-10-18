s = input("Введите строку: ")
words = s.split()
count = 0

for w in words:
    cleaned = w.strip(".,!?;:").lower()
    if cleaned == "":
        continue
    if cleaned.startswith(cleaned[0]) and cleaned.endswith(cleaned[0]):
        print(cleaned)
        count += 1

if count == 0:
    print("Нет совпадений")
print("Количество:", count)
