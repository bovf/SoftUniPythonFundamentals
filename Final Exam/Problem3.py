distributors = {}
clients = {}

while True:
    command = input()
    if command == "End":
        break

    command = command.split()

    operation = command[0]
    name = command[1]
    money = float(command[2])

    if operation == "Deliver":
        if name not in distributors.keys():
            distributors[name] = money
        else:
            distributors[name] += money

    elif operation == "Return":
        if name not in distributors.keys():
            pass
        else:
            if money > distributors[name]:
                pass
            else:
                distributors[name] -= money

    elif operation == "Sell":
        if name not in clients.keys():
            clients[name] = money
        else:
            clients[name] += money

money_total = 0

for client in sorted(clients.keys()):
    money_total += clients[client]
    print(f"{client}: {clients[client]:.2f}")
print(f"-----------")
for distributor in sorted(distributors.keys()):
    if not distributors[distributor] == 0:
        print(f"{distributor}: {distributors[distributor]:.2f}")
print(f"-----------")
print(f"Total Income: {money_total:.2f}")
