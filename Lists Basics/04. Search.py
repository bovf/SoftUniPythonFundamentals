n = int(input())
key_word = input()

list_with_filter = []
list_without_filter = []

key_word_in_sentence = False
word = str

for _ in range(n):
    sentence = input()
    list_without_filter.append(sentence)
    words_list = sentence.split(" ")
    for word_number in range(len(words_list)):
        word = words_list[word_number]
        if word == key_word:
            key_word_in_sentence = True
    if key_word_in_sentence:
        list_with_filter.append(sentence)
    else:
        pass
    key_word_in_sentence = False
print(list_without_filter)
print(list_with_filter)
