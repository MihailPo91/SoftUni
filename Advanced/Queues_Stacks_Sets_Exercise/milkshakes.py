from collections import deque

chocolate = [int(x) for x in input().split(', ')]
cups_of_milk = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while milkshakes < 5:
    if not chocolate or not cups_of_milk:
        break

    current_chocolate = chocolate.pop()
    current_cup_of_milk = cups_of_milk.popleft()

    if current_chocolate <= 0 and current_cup_of_milk <= 0:
        continue

    if current_chocolate <= 0:
        cups_of_milk.appendleft(current_cup_of_milk)
        continue

    if current_cup_of_milk <= 0:
        chocolate.append(current_chocolate)
        continue

    if current_chocolate != current_cup_of_milk:
        chocolate.append(current_chocolate - 5)
        cups_of_milk.append(current_cup_of_milk)

    else:
        milkshakes += 1


if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
    if chocolate:
        print("Chocolate:", end=' ')
        print(*chocolate, sep=', ')
    else:
        print('Chocolate: empty')
    if cups_of_milk:
        print("Milk:", end=' ')
        print(*cups_of_milk, sep=', ')
    else:
        print('Milk: empty')

else:
    print('Not enough milkshakes.')
    if chocolate:
        print("Chocolate:", end=' ')
        print(*chocolate, sep=', ')
    else:
        print('Chocolate: empty')
    if cups_of_milk:
        print("Milk:", end=' ')
        print(*cups_of_milk, sep=', ')
    else:
        print('Milk: empty')