first = input()
second = input()
result = ""

while first in second:
    second = second.replace(first, "")

print(second)