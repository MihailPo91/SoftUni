def out_of_bounds(row, col, rows, cols):
    if row < 0:
        row = rows - 1
    if col < 0:
        col = cols - 1
    if row == rows:
        row = 0
    if col == cols:
        col = 0
    return row, col


def get_next_move(row, col, command):
    if command == 'up':
        row -= 1
    elif command == 'down':
        row += 1
    elif command == 'left':
        col -= 1
    elif command == 'right':
        col += 1

    return out_of_bounds(row, col, rows, cols)


rows = 6
cols = 6

matrix = [[x for x in input().split()] for row in range(rows)]

rover_row = 0
rover_col = 0

water = 0
metal = 0
concrete = 0
broken = False

for row in range(len(matrix)):
    for col in range(cols):
        if matrix[row][col] == 'E':
            rover_row = row
            rover_col = col

commands = input().split(', ')

for command in commands:
    rover_row, rover_col = get_next_move(rover_row, rover_col, command)

    if matrix[rover_row][rover_col] == 'R':
        broken = True
        break
    elif matrix[rover_row][rover_col] == 'W':
        print(f'Water deposit found at ({rover_row}, {rover_col})')
        water += 1
    elif matrix[rover_row][rover_col] == 'M':
        print(f'Metal deposit found at ({rover_row}, {rover_col})')
        metal += 1
    elif matrix[rover_row][rover_col] == 'C':
        print(f'Concrete deposit found at ({rover_row}, {rover_col})')
        concrete += 1


if broken:
    print(f"Rover got broken at ({rover_row}, {rover_col})")

if water > 0 and metal > 0 and concrete > 0:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')
