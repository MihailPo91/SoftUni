items = input().split("|")
budget = float(input())
profit = 0
new_item_prices = []
data_prices = []
condition = False

for item in items:
    current_item_data = item.split("->")
    category = current_item_data[0]
    price = float(current_item_data[1])
    condition = False

    if category == "Clothes":
        if price <= 50:
            condition = True
    elif category == "Shoes":
        if price <= 35:
            condition = True
    elif category == "Accessories":
        if price <= 20.50:
            condition = True

    if condition:
        if budget >= price:
            budget -= price
            profit += price * 0.40
            new_price = price + (price * 0.40)
            new_item_prices.append(new_price)
            data_prices.append(f"{new_price:.2f}")


print(" ".join(data_prices))
print(f"Profit: {profit:.2f}")

total_sum = budget + sum(new_item_prices)
if total_sum >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
