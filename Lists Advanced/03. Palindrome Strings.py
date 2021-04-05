def check_if_string_palindrome(string):
    if string == (string[::-1]):
        return True
    else:
        return False


def check_for_word(keyword, word_to_check):
    if keyword == word_to_check:
        return 1
    else:
        return 0


sentence = input()
keyword_search = input()

sentence_list = sentence.split(" ")
palindrome_list = []
palindromes_found = 0

for word in sentence_list:
    if check_if_string_palindrome(word):
        palindrome_list.append(word)

    palindromes_found += check_for_word(keyword_search, word)

print(palindrome_list)
print(f"Found palindrome {palindromes_found} times")
