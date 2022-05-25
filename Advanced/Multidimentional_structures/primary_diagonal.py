def get_primary_diagonal_sum(matrix):
    the_sum = 0
    n = len(matrix)
    for r in range(n):
        for c in range(n):
            if c == r:
                the_sum += matrix[r][c]

    return the_sum


n = int(input())
matrix = [[int(x) for x in input().split(' ')] for _ in range(n)]

print(get_primary_diagonal_sum(matrix))
