raw_input = input("Целые числа через пробел: ").split()

numbers = []
for part in raw_input:
    numbers.append(int(part))

selected_numbers = []
for number in numbers:
    if number % 2 == 0:
        selected_numbers.append(number)

count = len(selected_numbers)
total_sum = sum(selected_numbers)
sorted_copy = sorted(selected_numbers)

print(f"Выборка: {selected_numbers}")
print(f"Количество: {count}")
print(f"Сумма: {total_sum}")
print(f"Отсортированная копия: {sorted_copy}")
