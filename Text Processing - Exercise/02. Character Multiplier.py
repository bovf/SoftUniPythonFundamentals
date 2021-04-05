words = input().split()
first_word_chars = []
second_word_chars = []
sum_chars = 0

words = [word for word in sorted(words, key=lambda element: len(element), reverse=True)]

for char in words[0]:
    first_word_chars.append(ord(char))

for char in words[1]:
    second_word_chars.append(ord(char))

for char in range(len(second_word_chars)):
    sum_chars += first_word_chars[char] * second_word_chars[char]

for char in range(len(first_word_chars), len(second_word_chars), -1):
    sum_chars += first_word_chars[char - 1]

print(sum_chars)
