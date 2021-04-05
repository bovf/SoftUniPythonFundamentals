numbers = input()

number_list_str = numbers.split(", ")
numbers_list_int = []

for number in number_list_str:
    number_int = int(number)
    numbers_list_int.append(number_int)


def is_it_palindrome(num):
    temp = num
    rev = 0
    while num > 0:
        digit = num % 10
        rev = 10 * rev + digit
        num = num // 10
    if rev == temp:
        print("True")
    else:
        print("False")


for number in numbers_list_int:
    is_it_palindrome(number)
