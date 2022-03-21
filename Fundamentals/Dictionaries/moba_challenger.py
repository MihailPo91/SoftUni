player_ranking = {}
total_skill_tracker = {}

while True:
    input_line = input()
    if input_line == "Season end":
        break

    if '->' in input_line:
        add_data = input_line.split(' -> ')
        player = add_data[0]
        position = add_data[1]
        skill = int(add_data[2])

        if player not in player_ranking:
            player_ranking[player] = {position: skill}
            total_skill_tracker[player] = skill

        elif player in player_ranking and position not in player_ranking.get(player):
            player_ranking[player][position] = skill
            total_skill_tracker[player] += skill

        else:
            if player_ranking[player][position] < skill:
                player_ranking[player][position] = 0
                player_ranking[player][position] += skill
                total_skill_tracker[player] -= total_skill_tracker[player]
                total_skill_tracker[player] += skill

    elif 'vs' in input_line:
        duel = input_line.split(' vs ')
        player_1 = duel[0]
        player_2 = duel[1]
        player_1_dict = {}
        player_2_dict = {}

        if player_1 in player_ranking and player_2 in player_ranking:
            for key, value in player_ranking.items():
                if key == player_1:
                    for position, points in value.items():
                        player_1_dict[position] = points

                elif key == player_2:
                    for position, points in value.items():
                        player_2_dict[position] = points

            for p, s in player_1_dict.items():
                if p in player_2_dict:
                    if player_1_dict[p] > player_2_dict[p]:
                        del player_ranking[player_2]
                        del total_skill_tracker[player_2]
                        break
                    elif player_2_dict[p] > player_1_dict[p]:
                        del player_ranking[player_1]
                        del total_skill_tracker[player_1]
                        break


total_points = dict(sorted(total_skill_tracker.items(), key=lambda x: (-x[1], x[0])))
for player, points in total_points.items():
    print(f'{player}: {points} skill')
    for key, value in player_ranking.items():
        value = dict(sorted(value.items(), key=lambda x: (-x[1], x[0])))
        if player == key:
            for position, skill in value.items():
                print(f'- {position} <::> {skill}')