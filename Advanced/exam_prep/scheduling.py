tasks = [int(x) for x in input().split(', ')]
target = int(input())
lowest = min(tasks)
time = 0
target_done = False

while True:
    if target_done:
        break

    for i, task in enumerate(tasks):
        if task == lowest:
            if i == target:
                time += task
                target_done = True
                break
            time += task
            lowest = task
            tasks[i] = 1000000

    lowest = min(tasks)


print(time)