def primary_diagonal(matrix):
    size = len(matrix)
    diagonal_values = []
    for i in range(size):
        diagonal_values.append(matrix[i][i])
    return diagonal_values


def secondary_diagonal(matrix):
    size = len(matrix)
    diagonal_values = []
    for i in range(size):
        diagonal_values.append(matrix[i][size - 1 - i])
    return diagonal_values


n = int(input())

matrix = [[int(x) for x in input().split(', ')] for row in range(n)]

primary_diagonal_rdy = ', '.join(list(map(str, primary_diagonal(matrix))))
secondary_diagonal_rdy = ', '.join(list(map(str, secondary_diagonal(matrix))))

print(f'Primary diagonal: {primary_diagonal_rdy}. Sum: {sum(primary_diagonal(matrix))}')
print(f'Secondary diagonal: {secondary_diagonal_rdy}. Sum: {sum(secondary_diagonal(matrix))}')