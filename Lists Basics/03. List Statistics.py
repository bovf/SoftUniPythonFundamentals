n = int(input())

positive_numbers = []
negative_numbers = []
count_positives = 0
sum_of_negatives = 0

for _ in range(n):
    number = int(input())
    if number < 0:
        negative_numbers.append(number)
        sum_of_negatives += number
    else:
        positive_numbers.append(number)
        count_positives += 1

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}")
