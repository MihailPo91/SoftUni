n = int(input())
ss = set()

for _ in range(n):
    name = input()
    ss.add(name)

[print(name) for name in ss]
