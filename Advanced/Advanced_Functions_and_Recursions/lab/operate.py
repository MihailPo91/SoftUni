def operate(operator, *args):
    def add(*args):
        return sum(args)

    def subtract(x, *args):
        result = x
        for n in args:
            result -= n
        return result

    def multiply(*args):
        result = 1
        for n in args:
            result *= n
        return result

    def divide(x, *args):
        result = x
        for n in args:
            result /= n
        return result

    if operator == '+':
        return add(*args)
    elif operator == '-':
        return subtract(*args)
    elif operator == '*':
        return multiply(*args)
    elif operator == '/':
        return divide(*args)


print(operate("-", 3, 4, 5))