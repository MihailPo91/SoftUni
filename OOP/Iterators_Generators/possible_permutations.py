from itertools import permutations


def possible_permutations(data):
    for result in permutations(data):
        yield list(result)


[print(n) for n in possible_permutations([1, 2, 3])]
