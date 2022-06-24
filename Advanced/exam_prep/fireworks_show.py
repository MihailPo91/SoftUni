from collections import deque

firework_effects = deque([int(x) for x in input().split(', ')])
explosives = [int(x) for x in input().split(', ')]
perfect_show = False

fireworks = {
    'Palm': 0,
    'Willow': 0,
    'Crossette': 0
}

while firework_effects and explosives:
    firework = firework_effects.popleft()
    explosive = explosives.pop()

    if explosive <= 0:
        firework_effects.appendleft(firework)
        continue

    if firework <= 0:
        explosives.append(explosive)
        continue


    total_power = firework + explosive

    if total_power % 3 == 0 and total_power % 5 != 0:
        fireworks['Palm'] += 1
    elif total_power % 5 == 0 and total_power % 3 != 0:
        fireworks['Willow'] += 1
    elif total_power % 3 == 0 and total_power % 5 == 0:
        fireworks['Crossette'] += 1
    else:
        firework_effects.append(firework - 1)
        explosives.append(explosive)

    if fireworks['Palm'] >= 3 and fireworks['Willow'] >= 3 and fireworks['Crossette'] >= 3:
        perfect_show = True
        break

if perfect_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f'Firework Effects left: {", ".join([str(x) for x in firework_effects])}')
if explosives:
    print(f'Explosive Power left: {", ".join([str(x) for x in explosives])}')

for key in fireworks:
    print(f'{key} Fireworks: {fireworks[key]}')