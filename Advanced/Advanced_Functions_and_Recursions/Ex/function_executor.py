def func_executor(*args):
    result = []
    for f in args:
        current_function, params = f
        func_result = current_function(*params)
        result.append(f'{current_function.__name__} - {func_result}')
    return '\n'.join(result)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))


