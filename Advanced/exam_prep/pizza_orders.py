from collections import deque

orders = deque([int(x) for x in input().split(', ')])
makers = [int(x) for x in input().split(', ')]

pizza_made = 0

while orders and makers:
    order = orders.popleft()
    maker = makers.pop()

    if order <= 0 or order > 10:
        makers.append(maker)
        continue

    if maker < order:
        pizza_made += maker
        order -= maker
        orders.appendleft(order)
    else:
        pizza_made += order

if not orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {pizza_made}')
    print(f'Employees: {", ".join([str(x) for x in makers])}')
else:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join([str(x) for x in orders])}')