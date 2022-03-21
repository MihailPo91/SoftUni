data = input().split(" ")
bakery = {}

for i in range(0, len(data), 2):
    food = data[i]
    quantity = data[i + 1]

    bakery[food] = int(quantity)

print(bakery)
