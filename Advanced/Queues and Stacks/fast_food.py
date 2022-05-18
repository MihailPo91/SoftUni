from collections import deque

food_quantity = int(input())
orders = deque([int(x) for x in input().split()])
print(max(orders))

while food_quantity > 0 and orders:
    current_order = orders[0]
    if current_order <= food_quantity:
        food_quantity -= current_order
        orders.popleft()
    else:
        print(f'Orders left: {" ".join(list(map(str, orders)))}')
        break

if not orders:
    print('Orders complete')