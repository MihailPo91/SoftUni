orders_number = int(input())
total_price = 0

for order in range(orders_number):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    order_price = price_per_capsule * days * capsules_count
    print(f"The price for the coffee is: ${order_price:.2f}")
    total_price += order_price

print(f"Total: ${total_price:.2f}")
