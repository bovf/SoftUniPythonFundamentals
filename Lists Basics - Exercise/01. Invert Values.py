numbers = input()

numbers_list = numbers.split(" ")
inverted_numbers = []

for number in range(len(numbers_list)):
    inverted_number = -1 * int(numbers_list[number])
    inverted_numbers.append(inverted_number)

print(inverted_numbers)