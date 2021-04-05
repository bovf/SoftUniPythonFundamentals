def reverse(numbers_list, index_from, index_to):
    numbers_list[index_from: index_to] = reversed(numbers_list[index_from: index_to])


def remove(numbers_list, index_to):
    del numbers_list[0:(index_to)]


def sort(numbers_list, index_from, index_to):
    numbers_list[index_from: index_to] = sorted(numbers_list[index_from: index_to])


numbers = input().split(" ")

while True:
    command = input()
    if command == "end":
        break

    command_list = command.split(" ")

    if command_list[0] == "reverse":
        index_one = int(command_list[2])
        index_two = index_one + int(command_list[4])
        reverse(numbers, index_one, index_two)
    elif command_list[0] == "remove":
        index_one = int(command_list[1])
        remove(numbers, index_one)
    elif command_list[0] == "sort":
        index_one = int(command_list[2])
        index_two = index_one + int(command_list[4])
        sort(numbers, index_one, index_two)

print(", ".join(numbers))
