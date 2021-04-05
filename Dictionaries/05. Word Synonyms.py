n = int(input())

synonyms_dict = {}

for _ in range(n):
    word = input()
    synonym = input()

    if word not in synonyms_dict.keys():
        synonyms_dict[word] = []
        synonyms_dict[word].append(synonym)
    else:
        synonyms_dict[word].append(synonym)

for word in synonyms_dict.keys():
    print(f"{word} - {', '.join(synonyms_dict[word])}")
