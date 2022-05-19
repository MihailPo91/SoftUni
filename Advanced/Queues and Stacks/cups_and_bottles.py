from collections import deque

cups = deque([int(x) for x in input().split(' ')])
bottles = deque([int(x) for x in input().split(' ')])

wasted_litres = 0

while cups:
    if bottles:
        current_bottle = bottles.pop()
        current_cup = cups[0]
        if current_bottle > current_cup:
            cups.popleft()
            wasted_litres += (current_bottle - current_cup)
        elif current_cup > current_bottle:
            cups[0] -= current_bottle
        else:
            cups.popleft()
    else:
        print(f'Cups: {" ".join(map(str, cups))}')
        print(f'Wasted litters of water: {wasted_litres}')
        break

if bottles:
    print(f'Bottles: {" ".join(map(str, bottles))}')
    print(f'Wasted litters of water: {wasted_litres}')