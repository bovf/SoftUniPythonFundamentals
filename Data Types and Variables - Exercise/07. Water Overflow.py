water_tank_capacity = 255
is_overflown = False

n = int(input())

for _ in range(n):
    quantity_pour = int(input())
    if water_tank_capacity >= quantity_pour:
        water_tank_capacity -= quantity_pour
    else:
        print(f"Insufficient capacity!")
print(255 - water_tank_capacity)
