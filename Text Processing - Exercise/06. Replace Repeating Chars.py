text = input()
new_text = ""

for char_num in range(len(text) - 1):
    if not text[char_num] == text[char_num + 1]:
        new_text += text[char_num]
print(new_text + text[-1])
