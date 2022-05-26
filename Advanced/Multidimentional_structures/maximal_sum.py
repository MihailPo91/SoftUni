rows, cols = [int(x) for x in input().split()]

matrix = [[int(r) for r in input().split()] for c in range(rows)]
max_sum = float('-inf')
target_sub_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2]\
        + matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2]\
        + matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]

        if current_sum > max_sum:
            max_sum = current_sum
            start_row = row
            start_col = col

print(f'Sum = {max_sum}')
print(f'{matrix[start_row][start_col]} {matrix[start_row][start_col + 1]} {matrix[start_row][start_col + 2]}')
print(f'{matrix[start_row + 1][start_col]} {matrix[start_row + 1][start_col + 1]} {matrix[start_row + 1][start_col + 2]}')
print(f'{matrix[start_row + 2][start_col]} {matrix[start_row + 2][start_col + 1]} {matrix[start_row + 2][start_col + 2]}')