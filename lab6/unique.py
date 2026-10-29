line = input("Введите числа: ").strip()

if not line:
    print([])
else:
    numbers = [int(x) for x in line.split()]
    unique_list = []
    
    for num in numbers:
        if num not in unique_list:
            unique_list.append(num)
            
    print(unique_list)
