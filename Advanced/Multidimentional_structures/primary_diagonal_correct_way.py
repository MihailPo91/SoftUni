def get_primary_diagonal_sum(matrix):
    total_sum = 0
    n = len(matrix)
    for i in range(n):
        total_sum += matrix[i][i]
    return total_sum


n = int(input())
matrix = [[int(x) for x in input().split(' ')] for _ in range(n)]

print(get_primary_diagonal_sum(matrix))
