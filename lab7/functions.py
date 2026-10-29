def sum_digits(number):
    """Возвращает сумму цифр модуля числа."""
    n = abs(number)
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

def average(numbers):
    """Возвращает среднее значение списка или None, если список пуст."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def normalize_text(text):
    """Возвращает текст в нижнем регистре без лишних пробелов."""
    return " ".join(text.split()).lower()

def select_numbers(numbers, threshold):
    """
    Вариант 10: возвращает числа от минус порога до 0 включительно.
    """
    result = []
    for num in numbers:
        if -threshold <= num <= 0:
            result.append(num)
    return result

def is_palindrome(text):
    """Проверяет, является ли нормализованный текст палиндромом."""
    normalized = normalize_text(text)
    cleaned = normalized.replace(" ", "")
    if not cleaned:
        return False
    return cleaned == cleaned[::-1]
