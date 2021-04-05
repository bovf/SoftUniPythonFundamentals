number_input = input()
number_of_beggars = int(input())

number_list_str = number_input.split(", ")
number_list_int = []

beggar_sum_list = []

for _ in range(number_of_beggars):
    beggar_sum_list.append(0)

for number in number_list_str:
    number_int = int(number)
    number_list_int.append(number_int)

beggar_counter = 0

for number_position in range(len(number_list_int)):
    if beggar_counter > number_of_beggars - 1:
        beggar_counter = 0

    beggar_sum_list[beggar_counter] += number_list_int[number_position]
    beggar_counter += 1

print(beggar_sum_list)
