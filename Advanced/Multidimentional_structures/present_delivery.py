def move_to(row, col, direction):
    if direction == 'up':
        return row - 1, col
    elif direction == 'down':
        return row + 1, col
    elif direction == 'left':
        return row, col - 1
    elif direction == 'right':
        return row, col + 1


def around(row, col, matrix, presents, nice_kids):
    around_tiles = [
        [row - 1, col],
        [row + 1, col],
        [row, col - 1],
        [row, col + 1],
    ]
    for r, c in around_tiles:
        if matrix[r][c] == 'V':
            presents -= 1
            matrix[r][c] = '-'
            nice_kids -= 1
        elif matrix[r][c] == 'X':
            presents -= 1
            matrix[r][c] = '-'
    return presents, nice_kids, matrix


presents = int(input())
size = int(input())

santa_row = 0
santa_col = 0

nice_kids = 0

matrix = []

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'S':
            santa_row, santa_col = row, col
        elif row_elements[col] == 'V':
            nice_kids += 1
    matrix.append(row_elements)

nice_kids_at_start = nice_kids

while presents > 0:
    command = input()
    if command == "Christmas morning":
        break

    next_row, next_col = move_to(santa_row, santa_col, command)
    if 0 <= next_row < size and 0 <= next_col < size:
        matrix[santa_row][santa_col] = '-'
        santa_row, santa_col = next_row, next_col

        if matrix[santa_row][santa_col] == 'V':
            presents -= 1
            nice_kids -= 1
        elif matrix[santa_row][santa_col] == 'C':
            presents, nice_kids, matrix = around(santa_row, santa_col,matrix, presents, nice_kids)
            matrix[santa_row][santa_col] = '-'

matrix[santa_row][santa_col] = 'S'

if presents == 0 and nice_kids > 0:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row, sep=' ')

if nice_kids == 0:
    print(f"Good job, Santa! {nice_kids_at_start} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")