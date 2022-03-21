budget = float(input())
season = input()
money_spend = 0
destination = ""
rental = ""

if budget <= 100:
    destination = "Somewhere in Bulgaria"
    if season == "summer":
        rental = "Camp"
        money_spend = budget * 0.30
    elif season == "winter":
        rental = "Hotel"
        money_spend = budget * 0.70

elif 100 < budget <= 1000:
    destination = "Somewhere in Balkans"
    if season == "summer":
        rental = "Camp"
        money_spend = budget * 0.40
    elif season == "winter":
        rental = "Hotel"
        money_spend = budget * 0.80

elif budget > 1000:
    destination = "Somewhere in Europe"
    rental = "Hotel"
    money_spend = budget * 0.90

print(destination)
print(f"{rental} - {money_spend:.2f}")




