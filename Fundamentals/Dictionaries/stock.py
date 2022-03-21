products = input().split(" ")
searched_product = input().split(" ")
shop = {}

for i in range(0, len(products), 2):
    food = products[i]
    quantity = products[i + 1]
    shop[food] = quantity

for product in searched_product:
    if product in shop.keys():
        print(f"We have {shop[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

