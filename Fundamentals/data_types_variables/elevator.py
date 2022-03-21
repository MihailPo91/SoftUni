N = int(input())
P = int(input())
courses = N / P

if N % P != 0:
    courses += 1

print(int(courses))

