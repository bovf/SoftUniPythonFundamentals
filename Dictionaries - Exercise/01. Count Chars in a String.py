text = input().split()

chars_dict = {}

for word in text:
    for char in word:
        if char not in chars_dict.keys():
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1

for char in chars_dict.keys():
    print(f"{char} -> {chars_dict[char]}")