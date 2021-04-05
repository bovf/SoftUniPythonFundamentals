key_materials = ['fragments', 'motes', 'shards']
inventory_key_materials = {"fragments": 0, "motes": 0, "shards": 0}
inventory_junk_materials = {}

item_obtained = False
item_shadowmourne = False
item_valanyr = False
item_dragonwrath = False

while not item_obtained:
    loot = input().split()
    for command_number in range(0, len(loot), 2):
        quantity = int(loot[command_number])
        item = loot[command_number + 1].lower()
        if item not in key_materials:
            if item not in inventory_junk_materials.keys():
                inventory_junk_materials[item] = quantity
            else:
                inventory_junk_materials[item] += quantity

        else:
            if item not in inventory_key_materials.keys():
                inventory_key_materials[item] = quantity
            else:
                inventory_key_materials[item] += quantity

        for key_material in inventory_key_materials.keys():
            if inventory_key_materials[key_material] >= 250:
                item_obtained = True
                inventory_key_materials[key_material] -= 250
                if key_material == "fragments":
                    item_valanyr = True
                elif key_material == "shards":
                    item_shadowmourne = True
                elif key_material == "motes":
                    item_dragonwrath = True
                break
        if item_obtained:
            break

item_farmed = ""

if item_shadowmourne:
    item_farmed = "Shadowmourne"
elif item_valanyr:
    item_farmed = "Valanyr"
elif item_dragonwrath:
    item_farmed = "Dragonwrath"

inventory_key_materials = {k: v for k, v in sorted(inventory_key_materials.items()
                                                   , key=lambda item: item[1], reverse=True)}

inventory_junk_materials = {k: v for k, v in sorted(inventory_junk_materials.items()
                                                    , key=lambda item: item[0], reverse=False)}

print(f"{item_farmed} obtained!")

for item in inventory_key_materials.keys():
    print(f"{item}: {inventory_key_materials[item]}")
for item in inventory_junk_materials.keys():
    print(f"{item}: {inventory_junk_materials[item]}")
