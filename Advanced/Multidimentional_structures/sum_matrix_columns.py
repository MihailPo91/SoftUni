n, m = [int(x) for x in input().split(', ')]

matrix = [[i for i in [int(x) for x in input().split(' ')]] for _ in range(n)]

column_sums = [0] * m

for row_index in range(n):
    for column_index in range(m):
        column_sums[column_index] += matrix[row_index][column_index]

print(*column_sums, sep='\n')
