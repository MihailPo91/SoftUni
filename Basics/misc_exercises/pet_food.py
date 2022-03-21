import math

number_of_days = int(input())
amount_of_foood = float(input())
food_eaten = 0
food_eaten_by_dog = 0
food_eaten_by_cat = 0
biscuits_counter = 0

for day in range(1, number_of_days + 1):
    food_per_day = 0
    dog = int(input())
    cat = int(input())
    food_eaten_by_dog += dog
    food_eaten_by_cat += cat
    food_per_day += dog + cat
    food_eaten = food_eaten_by_dog + food_eaten_by_cat

    if day % 3 == 0:
        biscuits_counter += food_per_day * 0.10

percent_eaten_food = (food_eaten / amount_of_foood) * 100
percent_eaten_by_dog = (food_eaten_by_dog / food_eaten) * 100
percent_eaten_by_cat = (food_eaten_by_cat / food_eaten) * 100

print(f"Total eaten biscuits: {round(biscuits_counter)}gr.")
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_eaten_by_dog:.2f}% eaten from the dog.")
print(f"{percent_eaten_by_cat:.2f}% eaten from the cat.")
