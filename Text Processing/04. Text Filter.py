filter_words = input().split(", ")
text = input()

for word in filter_words:

    while word in text:
        text = text.replace(word, f"*" * len(word))

print(text)