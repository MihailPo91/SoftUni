from functools import wraps


def is_even(n):
    return True if n % 2 == 0 else False


def even_numbers(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return [x for x in result if is_even(x)]
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))