inventory = {}

while True:
    command = input()
    if command == "statistics":
        break
    else:
        product, quantity = command.split(": ")
        if product not in inventory.keys():
            inventory[product] = int(quantity)
        else:
            inventory[product] += int(quantity)

print(f"Products in stock:")
for product in inventory.keys():
    print(f"- {product}: {inventory[product]}")
print(f"Total Products: {len(inventory.keys())} \n"
      f"Total Quantity: {sum(inventory.values())}")
