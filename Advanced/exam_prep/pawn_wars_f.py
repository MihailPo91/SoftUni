def is_valid_index(row, col, matrix_rows, matrix_cols):
    if 0 <= row < matrix_rows and 0 <= col < matrix_cols:
        return True
    return False


def make_move(player, row, col, current_movement, mx):
    mx[row][col] = '-'
    new_row = row + current_movement
    mx[new_row][col] = player[0]
    return mx, new_row


def is_taking(row, col, current_movement, player, mx):
    global other_player, rows, cols
    if is_valid_index(row+current_movement, col + 1, rows, cols) \
            and (mx[row + current_movement][col + 1] == other_player[0].lower()
                 or mx[row + current_movement][col + 1] == other_player[0]):
        return row+current_movement, col+1
    elif is_valid_index(row+current_movement, col - 1, rows, cols) \
            and (mx[row + current_movement][col - 1] == other_player[0].lower()
                 or mx[row + current_movement][col - 1] == other_player[0]):
        return row+current_movement, col-1
    return False, False


def is_at_end(row, max_rows, current_player):
    if current_player == 'White' and row == 0:
        return current_player
    elif current_player == 'Black' and row == max_rows - 1:
        return current_player
    return False


rows = 8
cols = 8

matrix = [[x for x in input().split()] for row in range(rows)]

current_player = 'White'
other_player = 'Black'

current_row = 0
current_col = 0
other_row = 0
other_col = 0
current_direction = -1
other_direction = +1

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
            current_row = row
            current_col = col
        if matrix[row][col] == 'b':
            other_row = row
            other_col = col


while True:
    target_row, target_col = is_taking(current_row, current_col, current_direction, current_player, matrix)
    if target_row:
        print(f'Game over! {current_player} win, capture on {columns_letters[target_col]}{ranks[target_row]}.')
        break
    matrix, current_row = make_move(current_player, current_row, current_col, current_direction, matrix)
    queen_getter = is_at_end(current_row, rows, current_player)
    if queen_getter:
        print(f'Game over! {queen_getter} pawn is promoted to a queen at {columns_letters[current_col]}{ranks[current_row]}.')
        break

    current_row, other_row = other_row, current_row
    current_col, other_col = other_col, current_col
    current_player, other_player = other_player, current_player
    current_direction, other_direction = other_direction, current_direction
    continue
