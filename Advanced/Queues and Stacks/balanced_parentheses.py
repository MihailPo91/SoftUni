expression = list(input())

st = []

for c in range(len(expression)):
    current = expression[c]
    if expression[c] == '(' or expression[c] == '[' or expression[c] == '{':
        st.append(expression[c])
    else:
        if st[-1] == '(':
            if expression[c] != ')':
                print('NO')
                break
            else:
                if st:
                    st.pop()
        elif st[-1] == '[':
            if expression[c] != ']':
                print('NO')
                break
            else:
                if st:
                    st.pop()
        elif st[-1] == '{':
            if expression[c] != '}':
                print('NO')
                break
            else:
                if st:
                    st.pop()
else:
    print('YES')