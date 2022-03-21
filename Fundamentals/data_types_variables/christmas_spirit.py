quantity = int(input())
days = int(input())
christmas_spirit = 0
total_cost = 0
condition_5th_day = False

for i in range(1, days + 1):
    condition_5th_day = False

    if i % 11 == 0:
        quantity += 2

    if i % 2 == 0:
        total_cost += (quantity * 2)
        christmas_spirit += 5

    if i % 3 == 0:
        total_cost += (quantity * 5) + (quantity * 3)
        christmas_spirit += 13
        condition_5th_day = True

    if i % 5 == 0:
        total_cost += (quantity * 15)
        christmas_spirit += 17

        if condition_5th_day:
            christmas_spirit += 30
    if i % 10 == 0:
        christmas_spirit -= 20
        total_cost += 23
        if i == days:
            christmas_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {christmas_spirit}")


