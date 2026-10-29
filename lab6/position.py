line = input("Введите числа: ").strip()

if not line:
    print("Нет данных")
else:
    numbers = [int(x) for x in line.split()]
    max_val = max(numbers)
    
    positions = []
    for index, value in enumerate(numbers):
        if value == max_val:
            positions.append(index)
            
    print(positions)
