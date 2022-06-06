import random


def raise_exception():
    chance = 0.7
    if random.random() < chance:
        raise ValueError('Invalid value')


exception = 0
for _ in range(100):
    try:
        raise_exception()
        print('No exceptions')
    except ValueError:
        print('Value error handled!')
        exception += 1

print(exception)