filter_word = input()
text = input()

while filter_word in text:
    text = text.replace(filter_word, "")

print(text)