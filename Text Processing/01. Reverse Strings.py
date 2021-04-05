while True:
    command = input()
    if command == "end":
        break
    reverse_string = ""
    for char in command:
        reverse_string = char + reverse_string

    print(f"{command} = {reverse_string}")
