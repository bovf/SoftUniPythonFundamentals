def multiply(a, b):
    return int(a * b)


def divide(a, b):
    return int(a / b)


def add(a, b):
    return int(a + b)


def subtract(a, b):
    return int(a - b)


def operation_checker(operation, a, b):
    if operation == "multiply":
        print(multiply(a, b))
    elif operation == "divide":
        print(divide(a, b))
    elif operation == "add":
        print(add(a, b))
    elif operation == "subtract":
        print(subtract(a, b))


operation = input()
first_number = int(input())
second_number = int(input())

operation_checker(operation, first_number, second_number)


