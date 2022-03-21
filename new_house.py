type_of_flowers = input()
quantity_of_flowers = int(input())
budget = int(input())
price = 0


if type_of_flowers == "Roses":
    price = quantity_of_flowers * 5
    if quantity_of_flowers > 80:
        price -= price * 0.10

elif type_of_flowers == "Dahlias":
    price = quantity_of_flowers * 3.8
    if quantity_of_flowers > 90:
        price -= price * 0.15

elif type_of_flowers == "Tulips":
    price = quantity_of_flowers * 2.8
    if quantity_of_flowers > 80:
        price -= price * 0.15

elif type_of_flowers == "Narcissus":
    price = quantity_of_flowers * 3
    if quantity_of_flowers < 120:
        price += price * 0.15

elif type_of_flowers == "Gladiolus":
    price = quantity_of_flowers * 2.5
    if quantity_of_flowers < 80:
        price += price * 0.20

left = abs(budget - price)
if price <= budget:
    print(f"Hey, you have a great garden with {quantity_of_flowers} {type_of_flowers} and {left:.2f} leva left.")
elif price > budget:
    print(f"Not enough money, you need {left:.2f} leva more.")