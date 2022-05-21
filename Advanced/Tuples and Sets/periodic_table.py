n = int(input())
periodic_table = set()

for _ in range(n):
    elements = input().split()
    for el in elements:
        periodic_table.add(el)

[print(element) for element in periodic_table]
