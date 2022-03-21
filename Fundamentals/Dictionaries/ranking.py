contest_passwords = {}
user_results = {}
user_total_points = {}

command = input()

while command != "end of contests":
    command = command.split(":")
    contest = command[0]
    password = command[1]

    contest_passwords[contest] = password
    command = input()

while True:
    submission = input().split("=>")
    if submission[0] == "end of submissions":
        break
    else:
        contest = submission[0]
        password = submission[1]
        name = submission[2]
        points = int(submission[3])

        if contest in contest_passwords and contest_passwords.get(contest) == password:

            if name in user_results.keys() and contest in user_results.get(name):

                current_points = user_results[name][contest]
                if current_points < points:
                    user_total_points[name] += (points - current_points)
                user_results[name][contest] = max(current_points, points)

            elif name in user_results:
                user_results[name][contest] = points
                user_total_points[name] += points

            else:
                user_results[name] = {contest: points}
                user_total_points[name] = points


print(f"Best candidate is {max(user_total_points.keys())} with total {(max(user_total_points.values()))} points.")
print("Ranking:")

for key in sorted(user_results.keys(), key=lambda x: x[1], reverse=True):
    print(f"{key}")
    for k, l in sorted(user_results[key].items(), key=lambda x: x[1], reverse=True):
        print(f"#  {k}", end=' -> ')
        print(f"{user_results[key][k]}")











