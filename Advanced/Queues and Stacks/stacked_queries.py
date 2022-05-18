st = []

num = int(input())

for _ in range(num):
    command = input()

    if command.startswith('1 '):
        items = command.split(' ')
        number = int(items[1])
        st.append(number)

    elif command == '2' and st:
        st.pop()

    elif command == '3' and st:
        print(max(st))

    elif command == '4' and st:
        print(min(st))

reversed_st = []
while st:
    reversed_st.append(st.pop())

print(*reversed_st, sep=', ')

