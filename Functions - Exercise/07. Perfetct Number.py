def is_it_perfect(num):

    divisor_sum = 0

    for divisor in range(1, num):
        if num % divisor == 0:
            divisor_sum += divisor

    if divisor_sum == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(is_it_perfect(number))
