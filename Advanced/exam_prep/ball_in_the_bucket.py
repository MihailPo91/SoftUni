def is_inbounds(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def get_throw_sum(row, col, board):
    score = 0

    if is_inbounds(row, col, len(board)):
        if board[row][col].isdigit():
            return False

        elif board[row][col] == 'B':
            for i in range(0, len(board)):
                if board[i][col].isdigit():
                    score += int(board[i][col])
            return score

    else:
        return False


size = 6
board = []

for row in range(size):
    row_details = input().split()
    board.append(row_details)

throws = 3
score = 0

for _ in range(3):
    row, col = [int(x) for x in input().strip("()").split(', ')]
    current_score = get_throw_sum(row, col, board)

    if current_score:
        score += current_score
        board[row][col] = '*'

if score < 100:
    print(f"Sorry! You need {100 - score} points more to win a prize.")
elif 100 <= score < 200:
    print(f"Good job! You scored {score} points, and you've won Football.")
elif 200 <= score < 300:
    print(f"Good job! You scored {score} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {score} points, and you've won Lego Construction Set.")
