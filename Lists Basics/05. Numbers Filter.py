n = int(input())

even_list = []
odd_list = []
negative_list = []
positive_list = []

for _ in range(n):
    number = int(input())
    if number < 0:
        negative_list.append(number)
    else:
        positive_list.append(number)
    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)

command = input()

if command == "even":
    print(even_list)
if command == "odd":
    print(odd_list)
if command == "negative":
    print(negative_list)
if command == "positive":
    print(positive_list)
