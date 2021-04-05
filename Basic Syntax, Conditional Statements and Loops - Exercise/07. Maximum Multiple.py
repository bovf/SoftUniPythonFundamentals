divisor = int(input())
bound = int(input())

max_num = int

for e in range(bound, 0, -1):
    if e % divisor == 0:
        max_num = e
        break
print(max_num)
