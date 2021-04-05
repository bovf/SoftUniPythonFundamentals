def get_chars_between(char_1, char_2):
    start, end = ord(char_1), ord(char_2)
    for char_num in range(start + 1, end):
        print(chr(char_num), end=" ")


first_char = input()
second_char = input()

get_chars_between(first_char, second_char)
