from functools import wraps
import unittest


def logged(func):
    @wraps(func)
    def wrapper(*args):
        function = func.__name__
        result = func(*args)
        to_return = f'you called {function}{args}\nit returned {result}'
        return to_return
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))



class LoggedTests(unittest.TestCase):
    def test_zero(self):
        @logged
        def func(*args):
            return 3 + len(args)
        result = func(4, 4, 4)
        self.assertEqual(result, 'you called func(4, 4, 4)\nit returned 6')


if __name__ == '__main__':
    unittest.main()
