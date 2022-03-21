percent_fats = int(input())
percent_proteins = int(input())
percent_carbs = int(input())
calories_total = int(input())
percent_water = int(input())

gram_fats = 9
gram_proteins = 4
gram_carbs = 4

fats = ((calories_total / 100) * percent_fats) / 9
proteins = ((calories_total / 100) * percent_proteins) / 4
carbs = ((calories_total / 100) * percent_carbs) / 4

food_total = fats + proteins + carbs
calories_per_gram = calories_total / food_total

waterless_calories = calories_per_gram - ((calories_per_gram / 100) * percent_water)

print(f"{waterless_calories:.4f}")