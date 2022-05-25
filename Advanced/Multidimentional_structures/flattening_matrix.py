n = int(input())

matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]
flattened = [i for row in matrix for i in row]

print(flattened)