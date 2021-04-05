def get_free_chairs(chair_rooms):
    chair_list = list(chair_rooms)
    is_there_chairs = True

    if len(chair_list) == 1:
        number_of_free_chairs = 0 - chair_list[0]
    else:
        number_of_free_chairs = len(chair_list) - 2 - int(chair_list[len(chair_list) - 1])

    if number_of_free_chairs < 0:
        is_there_chairs = False
        chairs_needed = abs(number_of_free_chairs)
        return chairs_needed, is_there_chairs
    else:
        chairs_needed = abs(number_of_free_chairs)
        return chairs_needed, is_there_chairs


rooms_with_chairs = int(input())

is_the_game_on = True
free_chairs = 0

for number in range(1, rooms_with_chairs + 1):
    room = input()
    chairs, is_there_free_chairs = get_free_chairs(room)
    if is_there_free_chairs:
        free_chairs += chairs
    else:
        is_the_game_on = False
        print(f"{chairs} more chairs needed in room {number}")

if is_the_game_on:
    print(f"Game On, {free_chairs} free chairs left")
