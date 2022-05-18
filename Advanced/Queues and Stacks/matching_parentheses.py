expression = input()

s = []

for ch in range(len(expression)):

    if expression[ch] == "(":
        s.append(ch)
    elif expression[ch] == ")":
        opening_index = s.pop()
        closing_index = ch + 1
        sub_expression = expression[opening_index:closing_index]
        print(sub_expression)
    else:
        pass
