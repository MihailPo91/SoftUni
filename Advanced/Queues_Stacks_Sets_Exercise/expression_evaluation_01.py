from collections import deque

expression = input().split()
numbs = deque()

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a // b,
}

for ch in expression:
    if ch in '+-*/':
        while len(numbs) > 1:
            first = numbs.popleft()
            second = numbs.popleft()
            result = operations[ch](first, second)
            numbs.appendleft(result)

    else:
        numbs.append(int(ch))

print(numbs[0])
