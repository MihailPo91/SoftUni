def is_valid_index(row, col, matrix_rows, matrix_cols):
    if 0 <= row < matrix_rows and 0 <= col < matrix_cols:
        return True
    return False


rows = 8
cols = 8

matrix = [[x for x in input().split()] for row in range(rows)]

white_row = 0
white_col = 0
black_row = 0
black_col = 0

ranks = {0: 8,
         1: 7,
         2: 6,
         3: 5,
         4: 4,
         5: 3,
         6: 2,
         7: 1,

}

columns_letters = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h',
}

for row in range(len(matrix)):
    for col in range(rows):
        if matrix[row][col] == 'w':
            white_row = row
            white_col = col
        if matrix[row][col] == 'b':
            black_row = row
            black_col = col


while True:

    if matrix[white_row - 1][white_col - 1] == 'b' and is_valid_index(white_row-1, white_col-1, rows, cols):
        print(f'Game over! White win, capture on {columns_letters[white_col - 1]}{ranks[white_row - 1]}.')
        break
    if matrix[white_row - 1][white_col + 1] == 'b' and is_valid_index(white_row-1, white_col+1, rows, cols):
        print(f'Game over! White win, capture on {columns_letters[white_col + 1]}{ranks[white_row - 1]}.')
        break
    matrix[white_row][white_col] = '-'
    white_row -= 1

    if white_row == 0:
        print(f'Game over! White pawn is promoted to a queen at {columns_letters[white_col]}{ranks[white_row]}.')
        break
    matrix[white_row][white_col] = 'w'

    if matrix[black_row + 1][black_col - 1] == 'w' and is_valid_index(black_row + 1, black_col - 1, rows, cols):
        print(f'Game over! Black win, capture on {columns_letters[black_col - 1]}{ranks[black_row + 1]}.')
        break
    if matrix[black_row + 1][black_col + 1] == 'w' and is_valid_index(black_row + 1, black_col + 1, rows, cols):
        print(f'Game over! Black win, capture on {columns_letters[black_col + 1]}{ranks[black_row + 1]}.')
        break
    matrix[black_row][black_col] = '-'
    black_row += 1

    if black_row == 7:
        print(f'Game over! Black pawn is promoted to a queen at {columns_letters[black_col]}{ranks[black_row]}.')
        break
    matrix[black_row][black_col] = 'b'
    continue
