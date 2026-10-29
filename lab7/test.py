from functions import average, normalize_text, sum_digits, select_numbers, is_palindrome

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text("  ПРИВЕТ   Мир  ") == "привет мир"
assert normalize_text("   ") == ""

original_list = [-5, 0, 2, 5]
original_copy = original_list.copy()

assert select_numbers(original_list, 2) == [0]

assert original_list == original_copy, "Ошибка: исходный список был изменён!"

assert select_numbers([], 5) == []

assert select_numbers([-4, -3, -2, -1, 0, 1], 3) == [-3, -2, -1, 0]

assert select_numbers([-2, -2, 0, 0], 2) == [-2, -2, 0, 0]

assert is_palindrome("А роза упала на лапу Азора") is True
assert is_palindrome("Привет") is False
assert is_palindrome("   ") is False
assert is_palindrome("") is False

print("Базовые и дополнительные проверки пройдены успешно!")
