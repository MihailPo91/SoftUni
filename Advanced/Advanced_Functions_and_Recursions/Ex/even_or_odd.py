def even_odd(*args):
    evens = []
    odds = []

    for n in args[:-1]:
        if n % 2 == 0:
            evens.append(n)
        else:
            odds.append(n)

    command = args[-1]

    if command == 'even':
        return evens
    elif command == 'odd':
        return odds


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))