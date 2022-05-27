def is_inside(size, row, col):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


def move_to(size, current_row, current_col, direction):
    if direction == 'up':
        if 0 <= current_row - 1 < size:
            current_row -= 1
        return current_row, current_col
    elif direction == 'down':
        if 0 <= current_row + 1 < size:
            current_row += 1
        return current_row, current_col
    elif direction == 'left':
        if 0 <= current_col - 1 < size:
            current_col -= 1
        return current_row, current_col
    elif direction == 'right':
        if 0 <= current_col + 1 < size:
            current_col += 1
        return current_row, current_col


size = int(input())

commands = [com for com in input().split()]

matrix = []
miner_row = 0
miner_col = 0
coal_collected = 0
coal_locations = []
exit_location = []

for row in range(size):
    row_elements = [i for i in input().split()]
    matrix.append(row_elements)

    for col in range(size):
        if row_elements[col] == 's':
            miner_row, miner_col = row, col
        elif row_elements[col] == 'c':
            coal_locations.append([row, col])
        elif row_elements[col] == 'e':
            exit_location = [row, col]


for direction in commands:
    new_row, new_col = move_to(size, miner_row, miner_col, direction)
    exited = False
    if matrix[new_row][new_col] == 'e':
        print(f"Game over! ({new_row}, {new_col})")
        exited = True
        break
    elif matrix[new_row][new_col] == 'c':
        coal_collected += 1
        coal_locations.remove([new_row, new_col])
        if not coal_locations:
            print(f"You collected all coal! ({new_row}, {new_col})")
            break
        matrix[new_row][new_col] = '*'
        miner_row, miner_col = new_row, new_col
    else:
        miner_row, miner_col = new_row, new_col

if coal_locations and not exited:
    print(f"{len(coal_locations)} pieces of coal left. ({miner_row}, {miner_col})")
