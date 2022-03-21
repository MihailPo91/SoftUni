number = (input())
n = str(number)
m = sorted(n, reverse=True)

for d, digit in enumerate(m):
    print(digit, end='')
