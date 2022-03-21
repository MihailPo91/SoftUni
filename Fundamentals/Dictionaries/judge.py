import operator
user_data = {}
contests = {}

while True:
    input_line = input()
    if input_line == "no more time":
        break

    user, contest, points = input_line.split(" -> ")
    if contest not in contests:
        contests[contest] = {}
    if user not in user_data:
        contests[contest][user] = int(points)
        user_data[user] = {contest: int(points)}
        user_data[user]['total_points'] = int(points)
    elif user in user_data and contest not in user_data.get(user):
        contests[contest][user] = int(points)
        user_data[user][contest] = int(points)
        user_data[user]['total_points'] += int(points)
    else:
        contests[contest][user] = int(points)
        current_points = int(user_data[user][contest])
        if int(points) > current_points:
            user_data[user]['total_points'] += (int(points) - current_points)
        user_data[user][contest] = max(current_points, int(points))

for contest, value in contests.items():
    print(f"{contest}: {(len(value))} participants")
    sorted_val = dict(sorted(value.items(), key=lambda item: -item[1]))
    for v, p in enumerate(sorted_val.items()):
        print(f"{v+1}. {p[0]} <::> {p[1]}")
print("Individual standings:")

for i, key in enumerate(sorted(user_data, key=operator.itemgetter(1), reverse=True)):
    print(f"{i+1}. {key} -> {user_data[key]['total_points']}")
