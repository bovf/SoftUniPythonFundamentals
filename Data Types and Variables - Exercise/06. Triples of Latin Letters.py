ascii_latin_start = 97
ascii_latin_end = 122

n = int(input()) + 97
result_3 = ""
result_1 = ""
result_2 = ""

char_counter = 0
for first_char in range(ascii_latin_start, n):
    first_letter = chr(first_char)
    result_1 += first_letter
    for second_char in range(ascii_latin_start, n):
        second_letter = chr(second_char)
        result_2 += result_1 + second_letter
        for third_char in range(ascii_latin_start, n):
            third_letter = chr(third_char)
            result_3 += result_2 + third_letter
            print(result_3)
            result_3 = ""
        result_2 = ""
    result_1 = ""
