number_of_people = int(input())
season = input()
total_costs = 0

if number_of_people <= 5:

    if season == "spring":
        price_per_person = 50
        total_costs = number_of_people * price_per_person

    elif season == "summer":
        price_per_person = 48.50
        total_costs = number_of_people * price_per_person
        total_costs -= total_costs * 0.15

    elif season == "autumn":
        price_per_person = 60
        total_costs = number_of_people * price_per_person

    elif season == "winter":
        price_per_person = 86
        total_costs = number_of_people * price_per_person
        total_costs += total_costs * 0.08

else:

    if season == "spring":
        price_per_person = 48
        total_costs = number_of_people * price_per_person

    elif season == "summer":
        price_per_person = 45
        total_costs = number_of_people * price_per_person
        total_costs -= total_costs * 0.15

    elif season == "autumn":
        price_per_person = 49.50
        total_costs = number_of_people * price_per_person

    elif season == "winter":
        price_per_person = 85
        total_costs = number_of_people * price_per_person
        total_costs += total_costs * 0.08

print(f"{total_costs:.2f} leva.")