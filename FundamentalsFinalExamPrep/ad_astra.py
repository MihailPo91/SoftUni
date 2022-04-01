import re

text = input()
pattern = r"([\|]|[#])(?P<food>[A-Za-z ]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d{1,5})\1"
matches = re.finditer(pattern, text)

food_items = []
calories = []
best_before = []
for match in matches:
    food_items.append(match.group("food"))
    best_before.append(match.group("date"))
    calories.append(int(match.group("calories")))

total_calories = sum(calories)
days = total_calories // 2000

print(f"You have food to last you for: {days} days!")
for i, item in enumerate(food_items):
    print(f"Item: {item}, Best before: {best_before[i]}, Nutrition: {calories[i]}")
