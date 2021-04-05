version_number_list = [int(number) for number in input().split(".")]

if version_number_list[2] != 9:
    version_number_list[2] += 1
else:
    if version_number_list[1] !=9:
        version_number_list[1] += 1
        version_number_list[2] = 0
    else:
        version_number_list[0] += 1
        version_number_list[1] = 0
        version_number_list[2] = 0

print(".".join([str(number) for number in version_number_list]))
