text = input()
new_text = ""

char_counter = 0
bomb_counter = 0

for char in text:
    if char == ">":
        bomb_counter += int(text[char_counter + 1])
        new_text += char
    elif bomb_counter > 0:
        bomb_counter -= 1
    else:
        new_text += char

    char_counter += 1

print(new_text)
