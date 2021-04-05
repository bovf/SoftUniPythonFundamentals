import re


def swap(string):
    string = list(string)
    string[0], string[-1] = string[-1], string[0]
    return "".join(string)


cyphered_words = input().split()

for word in cyphered_words:
    char_part = int((re.findall('\d+', word))[0])
    letter_part = str(re.findall('\D+', word)[0])
    ordered_letter_part = swap(letter_part)
    deciphered_word = chr(char_part) + ordered_letter_part

    print(deciphered_word, end=" ")
