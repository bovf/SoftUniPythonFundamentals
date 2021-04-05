numbers = input().split(", ")

even_numbers_indices = []

for index in range(len(numbers)):
    if int(numbers[index]) % 2 == 0:
        even_numbers_indices.append(index)

print(even_numbers_indices)
