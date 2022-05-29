def move_to(row, col, direction):
    if direction == 'up':
        return row - 1, col
    elif direction == 'down':
        return row + 1, col
    elif direction == 'left':
        return row, col - 1
    elif direction == 'right':
        return row, col + 1


size = int(input())

alice_row = 0
alice_col = 0

tea_collected = 0

matrix = []
for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'A':
            alice_row = row
            alice_col = col

    matrix.append(row_elements)

while tea_collected < 10:
    matrix[alice_row][alice_col] = '*'
    direction = input()
    next_row, next_col = move_to(alice_row, alice_col, direction)
    if next_row < 0 or next_row >= size or next_col < 0 or next_col >= size:
        break

    alice_row = next_row
    alice_col = next_col

    if matrix[alice_row][alice_col] == '.' or matrix[alice_row][alice_col] == '*':
        continue

    if matrix[alice_row][alice_col] == 'R':
        break

    tea_collected += int(matrix[alice_row][alice_col])

matrix[alice_row][alice_col] = '*'

if tea_collected >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row, sep=' ')
