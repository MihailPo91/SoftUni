from collections import deque


def gift_checker(n):
    if 100 <= n < 200:
        return 'Gemstone'
    elif 200 <= n < 300:
        return 'Porcelain Sculpture'
    elif 300 <= n < 400:
        return 'Gold'
    elif 400 <= n < 500:
        return 'Diamond Jewellery'
    elif n < 100:
        return 'less'
    else:
        return 'more'


materials = [int(x) for x in input().split()]
magics = deque([int(x) for x in input().split()])
success = False

gifts = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}

while materials and magics:
    gift_made = False
    mat = materials.pop()
    mag = magics.popleft()

    total_sum = mat + mag

    current = gift_checker(total_sum)

    if current != 'more' and current != 'less':
        gifts[current] += 1
        gift_made = True
    else:
        if current == 'more':
            total_sum /= 2
        else:
            if total_sum % 2 == 0:
                mat *= 2
                mag *= 3
                total_sum = mat + mag
            else:
                total_sum *= 2

    if not gift_made:
        current = gift_checker(total_sum)
        if current != 'more' and current != 'less':
            gifts[current] += 1

if (gifts['Gemstone'] > 0 and gifts['Porcelain Sculpture'] > 0) or\
        (gifts['Gold'] > 0 and gifts['Diamond Jewellery'] > 0):
    success = True


if success:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f'Materials left: {", ".join([str(x) for x in materials])}')
if magics:
    print(f'Magic left: {", ".join([str(x) for x in magics])}')

for key in sorted(gifts):
    if gifts[key] > 0:
        print(f'{key}: {gifts[key]}')