trip_price = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())
toys_total = number_puzzles + number_dolls + number_bears + number_minions + number_trucks
total_sum = number_puzzles * 2.6 + number_dolls * 3 + number_bears * 4.1 + number_minions * 8.2 + number_trucks * 2

if toys_total >= 50:
    total_sum -= total_sum * 0.25

rent = total_sum * 0.10
profit = total_sum - rent
diff = abs(profit - trip_price)

if profit >= trip_price:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")

