def is_outside(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return False
    return True


def get_next_position(row, col, matrix, command):
    if command == 'up':
        row -= 1
        if not is_outside(row, col, len(matrix)):
            return row, col
        row = len(matrix) - 1
        return row, col
    elif command == 'down':
        row += 1
        if not is_outside(row, col, len(matrix)):
            return row, col
        row = 0
        return row, col
    elif command == 'left':
        col -= 1
        if not is_outside(row, col, len(matrix)):
            return row, col
        col = len(matrix) - 1
        return row, col
    elif command == 'right':
        col += 1
        if not is_outside(row, col, len(matrix)):
            return row, col
        col = 0
        return row, col


size = int(input())
coins = 0
row = 0
col = 0
win = False
path = []

matrix = []

for r in range(size):
    row_details = input().split()
    matrix.append(row_details)
    for c in range(len(row_details)):
        if matrix[r][c] == 'P':
            row = r
            col = c

path.append([row, col])

while True:
    command = input()
    if command != 'up' and command != 'down' and command != 'left' and command != 'right':
        continue

    row, col = get_next_position(row, col, matrix, command)
    path.append([row, col])

    if matrix[row][col].isdigit():
        coins += int(matrix[row][col])
        matrix[row][col] = '-'
        if coins >= 100:
            win = True
            break
    elif matrix[row][col] == 'X':
        coins = int(coins / 2)
        break

if win:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")
print('Your path:')
for el in path:
    print(el)

