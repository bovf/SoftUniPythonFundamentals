def sum_nums(num_1, num_2):
    return num_1 + num_2


def subtract_nums(num_1, num_2):
    return num_1 - num_2


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

print(subtract_nums(sum_nums(num_1, num_2), num_3))
