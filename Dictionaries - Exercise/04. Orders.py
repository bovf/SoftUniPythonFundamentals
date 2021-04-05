products = {}

while True:
    command = input()
    if command == "buy":
        break
    else:
        command = command.split()

    product = command[0]
    price = float(command[1])
    quantity = int(command[2])
    price_and_quantity = [price, quantity]

    if product not in products.keys():
        products[product] = price_and_quantity
    else:
        if not price == products[product][1]:
            products[product][0] = price
            products[product][1] += quantity
        else:
            products[product][1] += quantity

for product in products.keys():
    print(f"{product} -> {products[product][0] * products[product][1]:.2f}")
