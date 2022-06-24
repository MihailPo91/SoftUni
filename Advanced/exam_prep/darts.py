def is_inbounds(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def get_score(row, col, board, type):
    score = 0
    if type == 'B':
        score = 501
        return score

    elif type.isdigit():
        score += int(board[row][col])
        return score

    elif type == 'D':
        for i in range(0, len(board)):
            if board[row][i].isdigit():
                score += int(board[row][i])
        for j in range(0, len(board)):
            if board[j][col].isdigit():
                score += int(board[j][col])
        return score * 2

    elif type == 'T':
        for i in range(0, len(board)):
            if board[row][i].isdigit():
                score += int(board[row][i])
        for j in range(0, len(board)):
            if board[j][col].isdigit():
                score += int(board[j][col])
        return score * 3


def get_throw_sum(row, col, board):
    if is_inbounds(row, col, len(board)):
        type = board[row][col]
        score = get_score(row, col, board, type)
        return score
    else:
        return False


player_one, player_two = input().split(', ')
size = 7
board = []
counter = 1
winner = ''

for row in range(size):
    row_details = input().split()
    board.append(row_details)

scores = {
    player_one: {'score': 501, 'throws': 1},
    player_two: {'score': 501, 'throws': 1}
}

while True:
    current_player = player_one if counter % 2 == 1 else player_two

    row, col = [int(x) for x in input().strip("()").split(', ')]
    current_score = get_throw_sum(row, col, board)
    if current_score:
        scores[current_player]['score'] -= current_score
        if scores[current_player]['score'] <= 0:
            winner = current_player
            break

    counter += 1
    scores[current_player]['throws'] += 1

print(f'{winner} won the game with {scores[current_player]["throws"]} throws!')