words_to_be_contained = input().split(", ")
words_to_check = input().split(", ")

words_match = []
for keyword in words_to_be_contained:
    for check_word in words_to_check:
        if check_word.__contains__(keyword):
            words_match.append(keyword)
            break

print(words_match)
