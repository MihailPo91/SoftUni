lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_shields = 0
total_repair_price = 0

for f in range(1, lost_fights_count + 1):
    if f % 2 == 0:
        total_repair_price += helmet_price
    if f % 3 == 0:
        total_repair_price += sword_price
        if f % 2 == 0:
            total_repair_price += shield_price
            broken_shields += 1
            if broken_shields == 2:
                total_repair_price += armor_price
                broken_shields = 0

print(f"Gladiator expenses: {total_repair_price:.2f} aureus")