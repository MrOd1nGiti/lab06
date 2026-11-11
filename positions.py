raw_input = input("Целые числа через пробел: ").split()

if not raw_input:
    print("Нет данных")
else:
    numbers = []
    for part in raw_input:
        numbers.append(int(part))
    
    max_val = max(numbers)
    positions = []
    
    for index, number in enumerate(numbers):
        if number == max_val:
            positions.append(index)
            
    print(positions)
