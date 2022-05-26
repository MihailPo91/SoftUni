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

matrix = [[int(x) for x in input().split(' ')] for row in range(n)]

end_result = sum(primary_diagonal(matrix)) - sum(secondary_diagonal(matrix))
print(abs(end_result))