string_input = input()
times = int(input())


def duplicate_string(string):
    return str(string)


full_result = string_input
for _ in range(times-1):
    full_result += duplicate_string(string_input)

print(full_result)
