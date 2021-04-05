import sys


def get_the_lower_number(min, new):
    if new <= min:
        return new
    else:
        return min


min_num = sys.maxsize
num_1 = int(input())
min_num = get_the_lower_number(min_num, num_1)
num_2 = int(input())
min_num = get_the_lower_number(min_num, num_2)
num_3 = int(input())
min_num = get_the_lower_number(min_num, num_3)

print(min_num)
