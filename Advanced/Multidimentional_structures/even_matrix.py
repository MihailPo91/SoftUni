rows = int(input())

matrix = [[i for i in [int(x) for x in input().split(', ')] if i % 2 == 0] for row in range(rows)]

print(matrix)