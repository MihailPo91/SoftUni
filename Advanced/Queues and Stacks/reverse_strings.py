original_string = input()

s = []

for c in original_string:
    s.append(c)

reverse_string = ''

while s:
    reverse_string += s.pop()

print(reverse_string)
