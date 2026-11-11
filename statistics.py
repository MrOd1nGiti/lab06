raw_input = input("Целые числа через пробел: ").split()

if not raw_input:
    print("Нет данных")
else:
    numbers = []
    for part in raw_input:
        numbers.append(int(part))
    
    count = len(numbers)
    total_sum = sum(numbers)
    min_val = min(numbers)
    max_val = max(numbers)
    average = total_sum / count
    
    print(f"Количество: {count}")
    print(f"Сумма: {total_sum}")
    print(f"Минимум: {min_val}")
    print(f"Максимум: {max_val}")
    print(f"Среднее: {average:.2f}")
