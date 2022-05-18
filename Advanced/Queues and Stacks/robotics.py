from collections import deque


def read_robots():
    result = {}
    robots_input = input().split(';')
    for robot_input in robots_input:
        robot_details = robot_input.split('-')
        name = robot_details[0]
        processing_time = int(robot_details[1])
        result[name] = processing_time
    return result


def to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds


def read_products():
    result = deque()
    while True:
        line = input()
        if line == 'End':
            break
        result.append(line)
    return result


def to_str_time(seconds):
    hour = seconds // 3600
    min = seconds % 3600 // 60
    sec = seconds % 3600 % 60
    return f"{hour:02d}:{min:02d}:{sec:02d}"


robots = read_robots()
available_robots = [k for k in robots.keys()]
processing_robots = {}

starting_time_parts = [int(x) for x in input().split(':')]

time_in_seconds = to_seconds(starting_time_parts[0], starting_time_parts[1], starting_time_parts[2])

products = read_products()

while products:
    time_in_seconds = (time_in_seconds + 1) % (24 * 60 * 60)

    for robot_name in [k for k in processing_robots.keys()]:
        processing_robots[robot_name] -= 1
        if processing_robots[robot_name] <= 0:
            processing_robots.pop(robot_name)

    current_product = products.popleft()
    for robot_name in available_robots:
        if robot_name not in processing_robots:
            print(f'{robot_name} - {current_product} [{to_str_time(time_in_seconds)}]')
            processing_robots[robot_name] = robots[robot_name]
            break
    else:
        products.append(current_product)
