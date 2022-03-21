fires = input().split("#")
water = int(input())
fire_value = 0
effort = 0
cells_list = []


for f, fire in enumerate(fires):
    current_fire = fire.split(" = ")
    if "High" in current_fire[0] and 81 <= int(current_fire[1]) <= 125:
        if water >= int(current_fire[1]):
            water -= int(current_fire[1])
        else:
            continue
        fire_value += int(current_fire[1])
        effort += int(current_fire[1]) * 0.25
        cells_list.append(current_fire[1])
    elif "Medium" in current_fire[0] and 51 <= int(current_fire[1]) <= 80:
        if water >= int(current_fire[1]):
            water -= int(current_fire[1])
        else:
            continue
        fire_value += int(current_fire[1])
        effort += int(current_fire[1]) * 0.25
        cells_list.append(current_fire[1])
    elif "Low" in current_fire[0] and 1 <= int(current_fire[1]) <= 50:
        if water >= int(current_fire[1]):
            water -= int(current_fire[1])
        else:
            continue
        fire_value += int(current_fire[1])
        effort += int(current_fire[1]) * 0.25
        cells_list.append(current_fire[1])
    if water == 0:
        break
print("Cells:")
for i, line in enumerate(cells_list):
    print(f" - {line}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {fire_value}")

