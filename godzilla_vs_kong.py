movie_budget = float(input())
number_extras = int(input())
clothing_price_per_extra = float(input())

decoration = movie_budget * 0.10
cloth_price = number_extras * clothing_price_per_extra

if number_extras >= 150:
    cloth_price -= cloth_price * 0.10

total_money_needed = decoration + cloth_price

diff = abs(movie_budget - total_money_needed)
if movie_budget >= total_money_needed:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
