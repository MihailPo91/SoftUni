import math

series = input()
length_per_episode = int(input())
lunch_break = int(input())

time_for_eating = lunch_break /8
time_for_relax = lunch_break /4
free_time = lunch_break - time_for_eating - time_for_relax

diff = abs(free_time - length_per_episode)

if free_time >= length_per_episode:
    print(f"You have enough time to watch {series} and left with {math.ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {math.ceil(diff)} more minutes.")
