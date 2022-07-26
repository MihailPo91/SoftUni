from functools import wraps


def vowel_filter(function):
    @wraps(function)
    def wrapper():
        result = function()
        to_return = [x for x in result if x in "eyuioa"]
        return to_return
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())