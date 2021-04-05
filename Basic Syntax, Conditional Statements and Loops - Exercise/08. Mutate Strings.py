first_word = str(input())
second_word = str(input())

new_word = ""
leftover_word = ""

do_print = bool

for i in range(len(first_word)):
    new_word += second_word[i]
    for e in range(i + 1, len(second_word)):
        leftover_word += first_word[e]
        do_print = True
    if first_word[i] == second_word[i]:
        do_print = False
    if do_print:
        print(f"{new_word}{leftover_word}")
    leftover_word = ""
