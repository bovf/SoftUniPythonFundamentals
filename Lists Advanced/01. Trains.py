number_of_wagons = int(input())

wagons_list = []

for _ in range(number_of_wagons):
    wagons_list.append(0)


def add(people, wagon_list):
    wagon_list[-1] += people


def insert(index, people, wagon_list):
    wagon_list[index] += people


def leave(index, people, wagon_list):
    wagon_list[index] -= people


while True:
    command = input()
    input_list = command.split(" ")

    if input_list[0] == "End":
        break

    if input_list[0] == "add":
        people = int(input_list[1])
        add(people, wagons_list)
    elif input_list[0] == "insert":
        index = int(input_list[1])
        people = int(input_list[2])
        insert(index, people, wagons_list)
    elif input_list[0] == "leave":
        index = int(input_list[1])
        people = int(input_list[2])
        leave(index, people, wagons_list)

print(wagons_list)
