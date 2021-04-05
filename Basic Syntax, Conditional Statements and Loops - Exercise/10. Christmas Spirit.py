# •	Ornament Set – 2$ a piece
# •	Tree Skirt – 5$ a piece
# •	Tree Garlands – 3$ a piece
# •	Tree Lights – 15$ a piece
quantity = int(input())
days_left = int(input())

money_spent = 0
christmas_spirit = 0

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15

for day in range(1, days_left+1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        money_spent += quantity * ornament_set
        christmas_spirit += 5
    if day % 3 == 0:
        money_spent += quantity * (tree_skirt + tree_garlands)
        christmas_spirit += 13
    if day % 5 == 0:
        money_spent += quantity * tree_lights
        christmas_spirit += 17
    if day % 3 == 0 and day % 5 == 0:
        christmas_spirit += 30
    if day % 10 == 0:
        money_spent += (tree_skirt + tree_garlands + tree_lights)
        christmas_spirit -= 20
    if day == days_left and days_left % 10 == 0:
        christmas_spirit -= 30

print(f"Total cost: {money_spent}\n"
      f"Total spirit: {christmas_spirit}")
