from collections import deque

qq = deque()

line = input().split()

for ch in line:

    if ch in '*+-/':

        if ch == '*':
            while len(qq) > 1:
                first = qq.popleft()
                second = qq.popleft()
                result = first * second
                qq.appendleft(result)
        elif ch == '+':
            while len(qq) > 1:
                first = qq.popleft()
                second = qq.popleft()
                result = first + second
                qq.appendleft(result)
        elif ch == '-':
            while len(qq) > 1:
                first = qq.popleft()
                second = qq.popleft()
                result = first - second
                qq.appendleft(result)
        elif ch == '/':
            while len(qq) > 1:
                first = qq.popleft()
                second = qq.popleft()
                result = int(first / second)
                qq.appendleft(result)
    else:
        qq.append(int(ch))

print(*list(qq), sep=' ')
