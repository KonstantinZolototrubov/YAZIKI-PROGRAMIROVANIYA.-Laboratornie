line = input("Введите числа: ").strip()

if not line:
    print("Нет данных")
else:
    numbers = [int(x) for x in line.split()]
    count = len(numbers)
    
    total = 0
    min_val = numbers[0]
    max_val = numbers[0]
    
    for num in numbers:
        total += num
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
            
    average = total / count
    
    print("Количество:", count)
    print("Сумма:", total)
    print("Минимум:", min_val)
    print("Максимум:", max_val)
    print(f"Среднее: {average:.2f}")
