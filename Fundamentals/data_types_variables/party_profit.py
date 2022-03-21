group_size = int(input())
days = int(input())
gold_total = 0


for day in range(1, days + 1):
    gold_total += 50
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    gold_total -= 2 * group_size
    if day % 3 == 0:
        gold_total -= 3 * group_size
    if day % 5 == 0:
        gold_total += 20 * group_size
        if day % 3 == 0:
            gold_total -= 2 * group_size

gold_per_companion = int(gold_total / group_size)
print(f"{group_size} companions received {gold_per_companion} coins each.")