mine = {}

while True:
    command = input()
    if command == "stop":
        break
    else:
        ore = command
        quantity = int(input())

        if ore not in mine.keys():
            mine[ore] = quantity
        else:
            mine[ore] += quantity

for ore in mine.keys():
    print(f"{ore} -> {mine[ore]}")
