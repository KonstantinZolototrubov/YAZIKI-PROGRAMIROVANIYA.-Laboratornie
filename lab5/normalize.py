s = input("Введите строку: ")
words = s.split()
normalized = " ".join(words)

print("Исходная длина:", len(s))
print("Новая длина:", len(normalized))
print("Нормализованный текст:", normalized)
print("Количество слов:", len(words))
