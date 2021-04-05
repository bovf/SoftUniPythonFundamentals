commands_number = int(input())
registered_users = {}

for _ in range(commands_number):
    parking_command = input().split()
    username = parking_command[1]
    if parking_command[0] == "register":
        plate_number = parking_command[2]
        if username not in registered_users.keys():
            registered_users[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")
    elif parking_command[0] == "unregister":
        if username not in registered_users.keys():
            print(f"ERROR: user {username} not found")
        else:
            del registered_users[username]
            print(f"{username} unregistered successfully")

for user in registered_users.keys():
    print(f"{user} => {registered_users[user]}")
