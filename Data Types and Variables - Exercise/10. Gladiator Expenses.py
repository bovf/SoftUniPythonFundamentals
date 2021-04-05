lost_fights = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0

times_shield_broke = 0

for lost_fight in range(1, lost_fights + 1):
    if lost_fight % 2 == 0:
        expenses += helmet_price
    if lost_fight % 3 == 0:
        expenses += sword_price
    if lost_fight % 3 == 0 and lost_fight % 2 == 0:
        expenses += shield_price
        times_shield_broke += 1
    if times_shield_broke == 2:
        expenses += armor_price
        times_shield_broke = 0

print(f"Gladiator expenses: {expenses:.2f} aureus")
