expression = input()

opening_brackets = []

pairs = {'(': ')', '[': ']', '{': '}'}

balanced = True
for ch in expression:
    if ch in '([{':
        opening_brackets.append(ch)
    else:
        if opening_brackets:
            last_opening_bracket = opening_brackets.pop()
            if pairs[last_opening_bracket] != ch:
                balanced = False
                break
        else:
            balanced = False
            break

if not balanced:
    print('NO')
else:
    if opening_brackets:
        print('NO')
    else:
        print('YES')
