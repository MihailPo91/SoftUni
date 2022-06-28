def shopping_cart(*args):
    cart_capacity = {'Soup': 3, 'Pizza': 4, 'Dessert': 2}
    cart = {'Soup': [], 'Pizza': [], 'Dessert': []}
    result = []
    for item in args:
        if item == 'Stop':
            break
        meal = item[0]
        product = item[1]

        if product not in cart[meal]:
            if len(cart[meal]) < cart_capacity[meal]:
                cart[meal].append(product)

    empty = True
    for key in cart:
        if len(cart[key]) > 0:
            empty = False
            break

    if empty:
        return 'No products in the cart!'
    else:
        for key, value in sorted(cart.items(), key=lambda x: (-len(x[1]), x[0])):
            result.append(f'{key}:')
            for v in sorted(cart[key]):
                result.append(f' - {v}')

        return '\n'.join(result)


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))


