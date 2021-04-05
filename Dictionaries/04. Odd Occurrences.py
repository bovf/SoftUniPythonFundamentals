words = input().split()

words_dict = {}
for word in words:
    word = word.lower()
    if word not in words_dict.keys():
        words_dict[word] = 1
    else:
        words_dict[word] += 1

for word in words_dict.keys():
    if not words_dict[word] % 2 == 0:
        print(word, end=" ")
