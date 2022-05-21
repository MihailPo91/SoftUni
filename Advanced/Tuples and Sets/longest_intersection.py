n = int(input())
target_intersection = set()

for _ in range(n):
    line = input().split('-')
    numbers = [int(n) for n in line[0].split(',')] + [int(n) for n in line[1].split(',')]
    s1 = set(range(numbers[0], numbers[1]+1))
    s2 = set(range(numbers[2], numbers[3]+1))
    intersection = s1.intersection(s2)
    if len(intersection) > len(target_intersection):
        target_intersection = intersection


print(f'Longest intersection is {list(target_intersection)} with length {len(target_intersection)}')