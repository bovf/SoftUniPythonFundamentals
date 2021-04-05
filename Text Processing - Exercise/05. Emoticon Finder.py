text = input()
emoticons = []

for char_num in range(len(text)):
    if text[char_num] == ":":
        emoticons.append(text[char_num + 1])

for emoticon in emoticons:
    print(f":{emoticon}")
