from collections import deque

words = deque(input().split())

primary_colours = {'red', 'blue', 'yellow'}
secondary_colours = {'orange', 'purple', 'green'}

collected_colours = []

while words:
    left = words.popleft()
    right = words.pop() if words else ""

    result = left + right
    if result in primary_colours or result in secondary_colours:
        collected_colours.append(result)
        continue

    result = right + left
    if result in primary_colours or result in secondary_colours:
        collected_colours.append(result)
        continue

    left = left[:-1]
    right = right[:-1]

    if left:
        words.insert(len(words) // 2, left)

    if right:
        words.insert(len(words) // 2, right)

result = []

validation_colours = {
    'orange': ['red', 'yellow'],
    'purple': ['red', 'blue'],
    'green': ['yellow', 'blue']
}

for colour in collected_colours:
    if colour in primary_colours:
        result.append(colour)
        continue

    is_collected = True
    for helper_colour in validation_colours[colour]:
        if helper_colour not in collected_colours:
            is_collected = False
            break

    if is_collected:
        result.append(colour)

print(result)