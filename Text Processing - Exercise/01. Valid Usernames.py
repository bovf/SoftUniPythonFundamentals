def check_for_length(word):
    if len(word) > 16 or len(word) < 3:
        return False
    else:
        return True


def check_chars(word):
    special_cases = ["-", "_"]
    for character in word:
        if character.isdigit():
            pass
        elif character.isalpha():
            pass
        elif character in special_cases:
            pass
        else:
            return False
    return True


usernames = input().split(", ")
valid_usernames = []

for username in usernames:
    is_valid = True

    if check_chars(username) and check_for_length(username):
        is_valid = True
    else:
        is_valid = False

    if is_valid:
        valid_usernames.append(username)

for valid_username in valid_usernames:
    print(f"{valid_username}")
