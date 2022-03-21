actor_name = input()
starting_points = float(input())
score_givers = int(input())

for num in range(score_givers):
    name = input()
    points_given = float(input())
    for char in name:
        starting_points += points_given / 2
    if starting_points >= 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {starting_points:.1f}!")
        break
else:
    print(f"Sorry, {actor_name} you need {(1250.5 - starting_points):.1f} more!")



