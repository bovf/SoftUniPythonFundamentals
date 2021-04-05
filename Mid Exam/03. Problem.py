def calculate_left(list_break, entry_index, item_type):
    sum_items = 0
    left_list = list_break[0:entry_index]
    if item_type == "cheap":
        for item in left_list:
            if item < list_break[entry_index]:
                sum_items += item
    else:
        for item in left_list:
            if item >= list_break[entry_index]:
                sum_items += item
    return sum_items


def calculate_right(list_break, entry_index, item_type):
    sum_items = 0
    right_list = list_break[entry_index + 1::]

    if item_type == "cheap":
        for item in right_list:
            if item < list_break[entry_index]:
                sum_items += item
    else:
        for item in right_list:
            if item >= list_break[entry_index]:
                sum_items += item
    return sum_items


numbers = [int(number) for number in input().split()]
entry = int(input())
vengeance = input()

left_sum = calculate_left(numbers, entry, vengeance)
right_sum = calculate_right(numbers, entry, vengeance)

if left_sum >= right_sum:
    print(f"Left - {left_sum}")
elif right_sum > left_sum:
    print(f"Right - {right_sum}")
