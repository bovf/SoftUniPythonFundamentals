multiple = int(input())
length = int(input())

multiples_list = []

for number in range(1, length + 1):
    result = number * multiple
    multiples_list.append(result)

print(multiples_list)
