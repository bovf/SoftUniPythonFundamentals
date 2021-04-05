gifts = input()

gifts_list = gifts.split(" ")

while True:
    command = input()
    if command == "No Money":
        break

    command_list = command.split(" ")

    if command_list[0] == "OutOfStock":
        for gift in gifts_list:
            if command_list[1] == gift:
                gift_index = gifts_list.index(gift)
                gifts_list[gift_index] = "None"

    if command_list[0] == "Required":
        required_index = int(command_list[2])
        if 0 <= required_index < len(gifts_list):
            gifts_list[required_index] = command_list[1]
        else:
            pass

    if command_list[0] == "JustInCase":
        gifts_list[-1] = command_list[1]

for gift in gifts_list:
    if gift == "None":
        pass
    else:
        print(gift, end=" ")
