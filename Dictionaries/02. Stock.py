stock = input().split()
commands = input().split()

inventory = {}

for product_number in range(0, len(stock), 2):
    key = stock[product_number]
    value = stock[product_number + 1]
    inventory[key] = int(value)

for command in commands:
    if command not in inventory.keys():
        print(f"Sorry, we don't have {command}")
    else:
        print(f"We have {inventory.get(command)} of {command} left")
