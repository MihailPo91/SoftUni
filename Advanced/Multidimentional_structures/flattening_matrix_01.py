n = int(input())
matrix = []

for i in range(n):
    ll = [int(x) for x in input().split(', ')]
    matrix.append(ll)

flattened = []

for row in matrix:
    for i in row:
        flattened.append(i)

print(flattened)