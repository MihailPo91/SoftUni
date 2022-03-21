current_price = 0
order = {}

while True:
    command = input()
    if command == "buy":
        break
    explode = command.split(" ")
    product = explode[0]
    price = float(explode[1])
    quantity = int(explode[2])

    if product not in order:
        order[product] = {}
        order[product]['quantity'] = quantity
        order[product]['price'] = price
        order[product]['total'] = order[product]['quantity'] * order[product]['price']

    else:
        order[product]['quantity'] += quantity
        order[product]['price'] = price
        order[product]['total'] = order[product]['quantity'] * order[product]['price']


for key, value in order.items():
    print(f"{key} -> {order[key]['total']:.2f}")
