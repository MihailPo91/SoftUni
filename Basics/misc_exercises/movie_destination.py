movie_budget = float(input())
destination = input()
season = input()
days = int(input())
price_per_day = 0
total_price = 0
money_enough = False

if season == "Winter":
    if destination == "London":
        price_per_day = 24000
        total_price = days * price_per_day

    if destination == "Sofia":
        price_per_day = 17000
        total_price = days * price_per_day
        total_price += total_price * 0.25

    if destination == "Dubai":
        price_per_day = 45000
        total_price = days * price_per_day
        total_price -= total_price * 0.30

if season == "Summer":
    if destination == "London":
        price_per_day = 20250
        total_price = days * price_per_day

    if destination == "Sofia":
        price_per_day = 12500
        total_price = days * price_per_day
        total_price += total_price * 0.25

    if destination == "Dubai":
        price_per_day = 40000
        total_price = days * price_per_day
        total_price -= total_price * 0.30

diff = abs(movie_budget - total_price)
if movie_budget >= total_price:
    money_enough = True
if money_enough:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")

