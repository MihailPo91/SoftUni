def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


def get_children(rows, cols, row, col):
    possible_children_coords = [
        [row - 1, col],
        [row, col - 1],
        [row, col + 1],
        [row + 1, col],

    ]
    result = []
    for child_row, child_col in possible_children_coords:
        if not is_outside(child_row, child_col, rows, cols):
            result.append([child_row, child_col])
    return result


def get_next_pos(row, col, command):
    if command == 'U':
        return row - 1, col
    elif command == 'D':
        return row + 1, col
    elif command == 'L':
        return row, col - 1
    elif command == 'R':
        return row, col + 1


rows, cols = [int(x) for x in input().split()]

bunnies = set()
player_row = 0
player_col = 0

matrix = []

for row in range(rows):
    row_elements = list(input())
    matrix.append(row_elements)
    for col in range(cols):
        if row_elements[col] == "P":
            player_row = row
            player_col = col
        elif row_elements[col] == "B":
            bunnies.add(f'{row} {col}')

commands = input()

won = False
dead = False

for command in commands:
    next_row, next_col = get_next_pos(player_row, player_col, command)
    matrix[player_row][player_col] = '.'
    if is_outside(next_row, next_col, rows, cols):
        won = True
    elif matrix[next_row][next_col] == 'B':
        player_col = next_col
        player_row = next_row
        dead = True
    else:
        matrix[next_row][next_col] = 'P'
        player_col = next_col
        player_row = next_row

    new_bunnies = set()

    for bunny in bunnies:
        bunny_row, bunny_col = [int(x) for x in bunny.split()]
        children = get_children(rows, cols, bunny_row, bunny_col)
        for child_row, child_col in children:
            new_bunnies.add(f'{child_row} {child_col}')
            matrix[child_row][child_col] = 'B'
            if child_row == player_row and child_col == player_col:
                dead = True

    bunnies = bunnies.union(new_bunnies)

    if won or dead:
        break

for row in matrix:
    print(''.join(row))

if won:
    print(f'won: {player_row} {player_col}')
else:
    print(f'dead: {player_row} {player_col}')
