def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    result = []
    bought = {}
    to_delete = {}
    basket_space = 5

    while kwargs:
        if basket_space == 0:
            break
        for key, value in kwargs.items():
            current_sum = kwargs[key][0] * kwargs[key][1]
            if current_sum <= budget:
                budget -= current_sum
                bought[key] = value
                result.append(f'You bought {key} for {current_sum:.2f} leva.')
                basket_space -= 1
                if basket_space == 0:
                    break
            else:
                to_delete[key] = value
        for key in to_delete:
            del kwargs[key]
        for key in bought:
            del kwargs[key]

    return "\n".join(result)


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

