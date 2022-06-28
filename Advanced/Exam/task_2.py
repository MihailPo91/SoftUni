player_one, player_two = input().split(', ')
size = 6
maze = []
counter = 1
resting = {
    player_one: False,
    player_two: False
}


for row in range(size):
    row_details = input().split()
    maze.append(row_details)

while True:

    current_player = player_one if counter % 2 == 1 else player_two
    other_player = player_two if counter % 2 == 1 else player_one

    if resting[current_player]:
        resting[current_player] = False
        counter += 1
        row, col = [int(x) for x in input().strip('()').split(', ')]
        continue

    row, col = [int(x) for x in input().strip('()').split(', ')]

    if maze[row][col] == 'E':
        print(f"{current_player} found the Exit and wins the game!")
        break

    elif maze[row][col] == 'T':
        print(f"{current_player} is out of the game! The winner is {other_player}.")
        break

    elif maze[row][col] == 'W':
        print(f"{current_player} hits a wall and needs to rest.")
        resting[current_player] = True

    counter += 1
