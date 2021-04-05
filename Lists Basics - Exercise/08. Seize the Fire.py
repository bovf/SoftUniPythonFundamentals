fires = input()
water = int(input())

fire_cells = fires.split("#")
effort = 0
total_fire = 0

print("Cells:")

for cell in fire_cells:
    cell_list = cell.split(" ")
    cell_type = cell_list[0]
    cell_number = int(cell_list[2])
    if cell_type == "High":
        if 80 < cell_number < 126:
            if cell_number <= water:
                print (f" - {cell_number}")
                total_fire += cell_number
                water -= cell_number
                effort += 0.25 * cell_number
    if cell_type == "Medium":
        if 50 < cell_number < 81:
            if cell_number <= water:
                print (f" - {cell_number}")
                total_fire += cell_number
                water -= cell_number
                effort += 0.25 * cell_number
    if cell_type == "Low":
        if 0 < cell_number < 51:
            if cell_number <= water:
                print (f" - {cell_number}")
                total_fire += cell_number
                water -= cell_number
                effort += 0.25 * cell_number

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
