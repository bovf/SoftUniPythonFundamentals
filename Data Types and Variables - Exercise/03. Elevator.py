import math


number_people = int(input())
elevator_capacity = int(input())

min_trips = math.ceil(number_people / elevator_capacity)

print(min_trips)