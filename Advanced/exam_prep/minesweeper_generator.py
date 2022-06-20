def is_valid_position(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def check_all_directions(row, col, matrix):
    mine_quantity = 0
    if is_valid_position(row-1, col, len(matrix)) and matrix[row-1][col] == '*':
        mine_quantity += 1
    if is_valid_position(row+1, col, len(matrix)) and matrix[row+1][col] == '*':
        mine_quantity += 1
    if is_valid_position(row, col-1, len(matrix)) and matrix[row][col-1] == '*':
        mine_quantity += 1
    if is_valid_position(row, col+1, len(matrix)) and matrix[row][col+1] == '*':
        mine_quantity += 1
    if is_valid_position(row-1, col-1, len(matrix)) and matrix[row-1][col-1] == '*':
        mine_quantity += 1
    if is_valid_position(row-1, col+1, len(matrix)) and matrix[row-1][col+1] == '*':
        mine_quantity += 1
    if is_valid_position(row+1, col-1, len(matrix)) and matrix[row+1][col-1] == '*':
        mine_quantity += 1
    if is_valid_position(row+1, col+1, len(matrix)) and matrix[row+1][col+1] == '*':
        mine_quantity += 1

    return mine_quantity


size = int(input())

matrix = [[0 for x in range(size)] for row in range(size)]

bombs_quantity = int(input())
bombs = []

for bomb in range(bombs_quantity):
    row, col = [int(x) for x in input().strip('()').split(', ')]
    matrix[row][col] = '*'

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] != '*':
            matrix[row][col] = check_all_directions(row, col, matrix)


for row in matrix:
    print(*row, sep=' ')