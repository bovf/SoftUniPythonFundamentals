max_stars = int(input())

for i in range(max_stars + 1):
    print(i * "*")
for i in range(max_stars - 1, -1, -1):
    print(i * "*")