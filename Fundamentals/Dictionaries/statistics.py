bakery = {}

while True:
    command = input()
    if command == "statistics":
        break
    data = command.split(": ")
    product = data[0]
    quantity = int(data[1])

    if product not in bakery:
        bakery[product] = 0
    bakery[product] += quantity


print("Products in stock:")
for key in bakery.keys():
    print(f"- {key}: {bakery[key]}")
print(f"Total Products: {len(bakery.keys())}")
print(f"Total Quantity: {sum(bakery.values())}")
