def order(drink ="coffee", quantity=3):
    if drink == "coffee":
        return quantity * 1.5
    elif drink == "water":
        return  quantity * 1
    elif drink == "coke":
        return quantity * 1.4
    elif drink == "snacks":
        return quantity * 2


current_order = input()
quantity_item = int(input())

result = order(current_order, quantity_item)
print(f"{result:.2f}")


