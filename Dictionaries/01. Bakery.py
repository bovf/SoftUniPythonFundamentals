elements = input().split()
bakery = {}

for element_number in range(0, len(elements), 2):
    key = elements[element_number]
    amount = elements[element_number + 1]
    bakery[key] = int(amount)

print(bakery)