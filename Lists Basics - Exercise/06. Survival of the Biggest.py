numbers_input = input()
number_list_str = numbers_input.split(" ")
n = int(input())

number_list_int = []

for number in number_list_str:
    number_int = int(number)
    number_list_int.append(number_int)

for _ in range(n):
    min_number = number_list_int[0]
    for number in number_list_int:
        if number < min_number:
            min_number = number
    number_list_int.remove(min_number)

print(number_list_int)
