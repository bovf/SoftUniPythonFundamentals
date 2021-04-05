rooms_with_chairs = int(input())
is_the_game_on = True
chairs_free = 0

for room_number in range(1, rooms_with_chairs + 1):
    chairs, people = input().split()
    people = int(people)
    chairs_left = abs(len(chairs) - people)
    if len(chairs) < people:
        print(f"{chairs_left} more chairs needed in room {room_number}")
        is_the_game_on = False
    else:
        chairs_free += chairs_left

if is_the_game_on:
    print(f"Game On, {chairs_free} free chairs left")
