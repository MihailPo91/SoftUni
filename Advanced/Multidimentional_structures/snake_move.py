from collections import deque

rows, cols = [int(x) for x in input().split()]

matrix = []

word = deque(input())

for row in range(rows):
    if row % 2 == 0:
        row_list = deque()
        while len(row_list) < cols:
            current_char = word.popleft()
            row_list.append(current_char)
            word.append(current_char)
        print("".join(row_list))
    else:
        row_list = deque()
        while len(row_list) < cols:
            current_char = word.popleft()
            row_list.appendleft(current_char)
            word.append(current_char)
        print("".join(row_list))




