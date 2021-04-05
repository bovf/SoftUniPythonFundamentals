numbers_int_list = [int(number) for number in input().split(", ")]

max_number = max(numbers_int_list)

if max_number % 10 > 0:
    groups = max_number // 10 + 1
else:
    groups = max_number // 10

for group in range(1, groups + 1):
    group_divisor = 10 * group
    group_list = []
    for number in numbers_int_list:
        if number <= group_divisor:
            group_list.append(number)

    print(f"Group of {group * 10}'s: {group_list}")
    numbers_int_list = [number for number in numbers_int_list if number not in group_list]
