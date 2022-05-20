import time
from random import shuffle

ll = list(range(1024 * 8))
shuffle(ll)

target = 8
targets = set()
values_map = {}

start = time.time()
for value in ll:
    if value in targets:
        p1 = value
        p2 = values_map[value]
        print(f'{p2} + {p1} = {target}')
    else:
        targets.add(target - value)
        values_map[target - value] = value

end = time.time()
print(f'{end - start} s')

target = 8

start = time.time()
for i1 in range(len(ll)):
    for i2 in range(i1 + 1, len(ll)):
        p1 = ll[i1]
        p2 = ll[i2]
        if p1 + p2 == target:
            print(f'{p1} + {p2} = {target}')

end = time.time()
print(f'{end - start} s')