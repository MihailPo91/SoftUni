contest_passwords = {}
user_submissions = {}
group_ranking = []

while True:
    input_line = input()
    if input_line == "end of contests":
        break
    contest, password = input_line.split(":")
    contest_passwords[contest] = password

while True:
    input_line = input()
    if input_line == "end of submissions":
        break

    contest, password, user, points = input_line.split("=>")

    if contest in contest_passwords and contest_passwords.get(contest) == password:

        if user in user_submissions and contest in user_submissions.get(user):
            current_points = user_submissions[user][contest]
            user_submissions[user][contest] = max(current_points, int(points))

        elif user in user_submissions:
            user_submissions[user][contest] = int(points)

        else:
            user_submissions[user] = {contest: int(points)}

for user in user_submissions:
    total_points = sum(user_submissions[user].values())
    group_ranking.append((user, total_points))

sorted_ranking = sorted(group_ranking, key=lambda item: -item[1])
print(f"Best candidate is {sorted_ranking[0][0]} with total {sorted_ranking[0][1]} points.")
print("Ranking:")
sorted_users = sorted(user for user in user_submissions.keys())
for user in sorted_users:
    user_subs = [u_s for u_s in sorted(user_submissions[user].items(), key=lambda item: -item[1])]
    output = [f"#  {contest} -> {points}" for (contest, points) in user_subs]
    print(user)
    print(*output, sep="\n")

