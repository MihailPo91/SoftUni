from functools import wraps


def cache(func):
    cached_values = {}

    @wraps(func)
    def wrapper(n):

        if n not in cached_values:
            cached_values[n] = func(n)

        return cached_values[n]

    wrapper.log = cached_values
    return wrapper


@cache
def fibonacci(n):

    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(33))
print(fibonacci.log)
