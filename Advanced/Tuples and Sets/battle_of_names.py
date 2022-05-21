n = int(input())
odds = set()
evens = set()

for row in range(1, n+1):
    name = input()
    name_sum = sum([ord(x) for x in name]) // row
    if name_sum % 2 == 0:
        evens.add(name_sum)
    else:
        odds.add(name_sum)

even_sum = sum(evens)
odd_sum = sum(odds)

if even_sum == odd_sum:
    result = odds.union(evens)
elif even_sum > odd_sum:
    result = odds.symmetric_difference(evens)
else:
    result = odds.difference(evens)

print(", ".join(list(map(str, result))))
