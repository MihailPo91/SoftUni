chicken_menu_price = 10.35
fish_menu_price = 12.40
vegan_menu_price = 8.15
delivery_price = 2.50

chicken = int(input())
fish = int(input())
vegan = int(input())
menu_price = chicken_menu_price * chicken + fish_menu_price * fish + vegan_menu_price * vegan
dessert = menu_price * 0.20

final_price = menu_price + dessert + delivery_price
print(final_price)