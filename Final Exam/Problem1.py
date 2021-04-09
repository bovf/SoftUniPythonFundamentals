import re


def make_upper(text, index):
    text[index] = text[index].upper()


def make_lower(text, index):
    text[index] = text[index].lower()


def insert(text, letter, index):
    text.insert(index, letter)


def replace(text, letter, value):
    for index, el in enumerate(text):
        if el == letter:
            text[index] = chr(ord(el) + value)


def validate(text):
    # at least 8, only digits letters and _, 1 upper, 1 lower, 1 digit
    text_to_string = "".join(text)
    error = ""
    pattern_upper = r"[A-Z]+"
    pattern_lower = r"[a-z]+"
    patter_digits = r"\d+"
    pattern_only_letters_digits_underscore = r"^[a-zA-Z0-9\_+]+$"
    if len(text) < 7:
        error += "Password must be at least 8 characters long!\n"
    if len(re.findall(pattern_only_letters_digits_underscore, text_to_string)) < 1:
        error += "Password must consist only of letters, digits and _!\n"
    if len(re.findall(pattern_upper, text_to_string)) < 1:
        error += "Password must consist at least one uppercase letter!\n"
    if len(re.findall(pattern_lower, text_to_string)) < 1:
        error += "Password must consist at least one lowercase letter!\n"
    if len(re.findall(patter_digits, text_to_string)) < 1:
        error += "Password must consist at least one digit!\n"
    return error.rstrip("\n")


password = list(input())

while True:
    command = input()
    if command == "Complete":
        break

    command = command.split()

    if command[0] == "Make":
        if command[1] == "Upper":
            make_upper(password, int(command[2]))
            print(''.join(password))
        elif command[1] == "Lower":
            make_lower(password, int(command[2]))
            print(''.join(password))
    elif command[0] == "Replace":
        replace(password, command[1], int(command[2]))
        print(''.join(password))
    elif command[0] == "Insert":
        insert(password, command[2], int(command[1]))
        print(''.join(password))
    elif command[0] == "Validation":
        print(validate(password))



