budget = float(input())
price_flour_kg = float(input())

money_left = budget
milk_left = 0
cozonacs = 0
coloured_eggs = 0

price_eggs_pack = 0.75 * price_flour_kg
price_milk_liter = price_flour_kg + 0.25 * price_flour_kg
price_cozonak = price_flour_kg + price_eggs_pack + price_milk_liter / 4

while money_left >= price_cozonak:

    cozonacs += 1
    milk_left -= 0.25
    coloured_eggs += 3
    if cozonacs % 3 == 0:
        coloured_eggs -= (cozonacs - 2)
    money_left -= price_cozonak

print(f"You made {cozonacs} cozonacs! Now you have {coloured_eggs} eggs and {money_left:.2f}BGN left.")
