def get_free_chairs(chair_rooms):
    chair_total = [chair for chair in chair_rooms if chair == "X"]
    chair_total = len(chair_total)
    chair_taken = [int(people) for people in chair_rooms if people != "X" and people != " "]
    chair_taken = chair_taken[0]
    is_there_chairs = True
    chairs_free = chair_total - chair_taken
    if chair_total < chair_taken:
        is_there_chairs = False
        return abs(chairs_free), is_there_chairs
    else:
        return abs(chairs_free), is_there_chairs


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
