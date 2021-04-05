import sys

n = int(input())

snowball_value = -sys.maxsize
best_snowball_snow = int
best_snowball_time = int
best_snowball_quality = int

for snowball in range(1, n + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    if snowball_value <= pow((snowball_snow / snowball_time), snowball_quality):
        snowball_value = int(pow((snowball_snow / snowball_time), snowball_quality))
        best_snowball_snow = snowball_snow
        best_snowball_time = snowball_time
        best_snowball_quality = snowball_quality

print(f"{best_snowball_snow} : {best_snowball_time} = {snowball_value} ({best_snowball_quality})")
