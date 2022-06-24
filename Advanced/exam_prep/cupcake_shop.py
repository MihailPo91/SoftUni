from collections import deque


def stock_availability(inventory, command, *args):
    inventory = deque(inventory)
    to_remove = []

    if command == 'delivery':
        for el in args:
            inventory.append(el)

    elif command == 'sell':
        if not args:
            inventory.popleft()
        else:
            if str(args[0]).isdigit():
                for _ in range(int(args[0])):
                    inventory.popleft()
            else:
                for el in inventory:
                    if el in args:
                        to_remove.append(el)
                for item in to_remove:
                    if item in inventory:
                        inventory.remove(item)

    inventory = list(inventory)

    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))