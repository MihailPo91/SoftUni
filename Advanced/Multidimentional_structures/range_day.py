def is_not_valid(matrix, row, col):
    return row < 0 or row >= 5 or col < 0 or col >= 5 or matrix[row][col] != '.'


def move_to(row, col, direction, steps):
    if direction == 'up':
        return row - steps, col
    elif direction == 'down':
        return row + steps, col
    elif direction == 'left':
        return row, col - steps
    elif direction == 'right':
        return row, col + steps


matrix = []

main_row = 0
main_col = 0
targets = 0

for row in range(5):
    row_elements = input().split()
    for col in range(5):
        if row_elements[col] == 'A':
            main_row, main_col = row, col
        elif row_elements[col] == 'x':
            targets += 1
    matrix.append(row_elements)

n = int(input())
targets_shot = []
matrix[main_row][main_col] = '.'

for i in range(n):
    line = input().split()
    command = line[0]

    if command == 'move':
        direction = line[1]
        steps = int(line[2])
        next_row, next_col = move_to(main_row, main_col, direction, steps)
        if is_not_valid(matrix, next_row, next_col):
            continue
        main_row, main_col = next_row, next_col

    elif command == 'shoot':
        direction = line[1]
        bullet_row, bullet_col = move_to(main_row, main_col, direction, 1)
        while 0 <= bullet_row < 5 and 0 <= bullet_col < 5:
            if matrix[bullet_row][bullet_col] == 'x':
                targets -= 1
                matrix[bullet_row][bullet_col] = '.'
                targets_shot.append([bullet_row, bullet_col])
                break
            bullet_row, bullet_col = move_to(bullet_row, bullet_col, direction, 1)

        if targets == 0:
            break

if targets > 0:
    print(f'Training not completed! {targets} targets left.')
else:
    print(f'Training completed! All {len(targets_shot)} targets hit.')
print(*targets_shot, sep='\n')