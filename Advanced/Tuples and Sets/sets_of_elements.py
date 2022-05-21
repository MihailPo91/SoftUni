n, m = tuple(map(int, input().split(' ')))
s1 = set()
s2 = set()

for _ in range(n):
    num = int(input())
    s1.add(num)

for _ in range(m):
    num = int(input())
    s2.add(num)

if len(s1) >= len(s2):
    intersection = s1 & s2
    [print(el) for el in intersection]
else:
    intersection = s2 & s1
    [print(el) for el in intersection]