years = int(input())
washing_machine_price = float(input())
toy_price = int(input())
toy_count = 0
money = 0


for num in range(years + 1):
    if num % 2 == 1:
        toy_count += 1
    elif num % 2 == 0 and num != 0:
        if num == 2:
            money += 10 - 1
        else:
            money += (num / 2 * 10) - 1

total_money = money + (toy_count * toy_price)
diff = abs(total_money - washing_machine_price)

if total_money >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
