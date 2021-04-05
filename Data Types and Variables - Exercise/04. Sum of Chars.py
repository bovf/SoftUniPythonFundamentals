n = int(input())

char_sum = 0

for _ in range(n):
    char = input()
    char_sum += ord(char)

print(f"The sum equals: {char_sum}")