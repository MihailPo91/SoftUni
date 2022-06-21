def can_capture(row, col, matrix):

    for position in range(row+1, len(matrix)):  # DOWN

        if matrix[position][col] == 'Q':
            break
        elif matrix[position][col] == 'K':
            return True

    for position in range(row-1, -1, -1):  # UP

        if matrix[position][col] == 'Q':
            break
        elif matrix[position][col] == 'K':
            return True

    for position in range(col+1, len(matrix)):  # RIGHT

        if matrix[row][position] == 'Q':
            break
        elif matrix[row][position] == 'K':
            return True

    for position in range(col-1, -1, -1):  # LEFT

        if matrix[row][position] == 'Q':
            break
        elif matrix[row][position] == 'K':
            return True

    for r, c in zip(range(row-1, -1, -1), range(col+1, 8)):  # UP RIGHT
        if matrix[r][c] == 'Q':
            break
        elif matrix[r][c] == 'K':
            return True

    for r, c in zip(range(row-1, -1, -1), range(col-1, -1, -1)):  # UP LEFT
        if matrix[r][c] == 'Q':
            break
        elif matrix[r][c] == 'K':
            return True

    for r, c in zip(range(row+1, 8), range(col+1, 8)):  # DOWN RIGHT
        if matrix[r][c] == 'Q':
            break
        elif matrix[r][c] == 'K':
            return True

    for r, c in zip(range(row+1, 8), range(col-1, -1, -1)):  # DOWN LEFT
        if matrix[r][c] == 'Q':
            break
        elif matrix[r][c] == 'K':
            return True

    return False


board = []
queens = []
king_position = (0, 0)

bad_quinnies = []

for row in range(8):
    row_items = input().split()
    for col in range(len(row_items)):
        if row_items[col] == 'Q':
            queens.append([row, col])
        elif row_items[col] == 'K':
            king_position = (row, col)
    board.append(row_items)


for queen in queens:
    if can_capture(queen[0], queen[1], board):
        bad_quinnies.append(queen)
        print(queen)

if not bad_quinnies:
    print('The king is safe!')

