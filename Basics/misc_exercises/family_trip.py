budget = float(input())
sleep_overs = int(input())
price_per_sleep_over = float(input())
percent_for_added_money = int(input())
money_is_enough = False

if sleep_overs > 7:
    price_per_sleep_over -= price_per_sleep_over * 0.05

money_spent = (sleep_overs * price_per_sleep_over)
pure_budget = budget - ((budget / 100) * percent_for_added_money)

diff = abs(pure_budget - money_spent)

if pure_budget >= money_spent:
    money_is_enough = True

if money_is_enough:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")

else:
    print(f"{diff:.2f} leva needed.")


