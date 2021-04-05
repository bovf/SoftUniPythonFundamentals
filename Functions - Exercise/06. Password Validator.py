def is_the_password_valid(password):
    is_it_valid = True
    if not 5 < len(password) < 10:
        is_it_valid = False
        print("Password must be between 6 and 10 characters")
    for char in password:
        if 47 < ord(char) < 58 or 64 < ord(char) < 91 or 96 < ord(char) < 123:
            pass
        else:
            is_it_valid = False
            print("Password must consist only of letters and digits")
            break

    digit_counter = 0
    for char in password:
        if 47 < ord(char) < 58:
            digit_counter += 1

    if digit_counter < 2:
        is_it_valid = False
        print("Password must have at least 2 digits")


    if is_it_valid:
        print("Password is valid")


password_input = input()

is_the_password_valid(password_input)
