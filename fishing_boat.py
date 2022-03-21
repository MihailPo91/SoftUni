budget = int(input())
season = input()
number_of_fishermen = int(input())


if season == "Spring":
    rent = 3000
    if number_of_fishermen <= 6:
        rent -= rent * 0.10
    elif 7 <= number_of_fishermen <= 11:
        rent -= rent * 0.15
    else:
        rent -= rent * 0.25
elif season == "Summer" or season == "Autumn":
    rent = 4200
    if number_of_fishermen <= 6:
        rent -= rent * 0.10
    elif 7 <= number_of_fishermen <= 11:
        rent -= rent * 0.15
    else:
        rent -= rent * 0.25
elif season == "Winter":
    rent = 2600
    if number_of_fishermen <= 6:
        rent -= rent * 0.10
    elif 7 <= number_of_fishermen <= 11:
        rent -= rent * 0.15
    else:
        rent -= rent * 0.25

if number_of_fishermen % 2 == 0 and not season == "Autumn":
    rent -= rent * 0.05

diff = abs(budget - rent)

if budget >= rent:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
