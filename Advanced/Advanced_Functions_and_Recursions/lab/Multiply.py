def multiply(*args):
    result = 1
    for v in args:
        result *= v
    return result


print(multiply(1, 4, 5))
