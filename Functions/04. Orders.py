def coffee():
    return 1.5


def water():
    return 1.00


def coke():
    return 1.40


def snacks():
    return 2.00


def order_checker(order):
    if order == "coffee":
        return coffee()
    elif order == "water":
        return water()
    elif order == "coke":
        return coke()
    elif order == "snacks":
        return snacks()


order = input()
times = int(input())

total_price = order_checker(order) * times

print(f"{total_price:.2f}")
