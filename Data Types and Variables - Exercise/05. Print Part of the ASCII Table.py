char_start = int(input())
char_end = int(input())

for char_num in range(char_start, char_end + 1):
    print(chr(char_num) + " ", end="")
