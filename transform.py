raw_input = input("Целые числа через пробел: ").split()

original_numbers = []
for part in raw_input:
    original_numbers.append(int(part))

transformed_numbers = []
for number in original_numbers:
    transformed_numbers.append(abs(number))

print(f"Исходный список: {original_numbers}")
print(f"Новый список: {transformed_numbers}")
