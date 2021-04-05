n = int(input())

is_it_special = bool
digit_sum = 0

for number in range(1, n + 1):
    for digit in range(len(str(number))):
        digit_sum += int(str(number)[digit])
    if digit_sum == 11 or digit_sum == 5 or digit_sum == 7:
        is_it_special = True
    else:
        is_it_special = False
    print(f"{number} -> {is_it_special}")
    digit_sum = 0
