num = float(input())

if num == 0:
    print("zero")

elif num > 0:
    if num < 1:
        print("small positive")
    elif 1000000 > num > 1:
        print("positive")
    elif num > 1000000:
        print("large positive")

elif num < 0:
    if num > -1:
        print("small negative")
    elif -1000000 < num < -1:
        print("negative")
    elif num < -1000000:
        print("large negative")
