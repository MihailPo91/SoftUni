def read_matrix():
    n, m = [int(x) for x in input().split(', ')]

    matrix = []

    for _ in range(n):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)

    return matrix


matrix = read_matrix()
print(sum([sum(row) for row in matrix]))
print(matrix)
