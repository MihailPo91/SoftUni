numbers_string = input()

dd = {}
numbers = [float(x) for x in numbers_string.split(' ')]

for n in numbers:
    if n not in dd:
        dd[n] = 0
    dd[n] += 1

for key, value in dd.items():
    print(f'{key:.1f} - {value} times')
