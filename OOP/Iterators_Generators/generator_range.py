def genrange(start, end):
    value = start
    while value <= end:
        yield value
        value += 1


print(list(genrange(1, 10)))