def get_started(player_one):
    while True:
        player_one_mark = input(f'{player_one}, pick X or O ').upper()
        if player_one_mark != 'X' and player_one_mark != "O":
            print('Please select X or O!')
            continue
        else:
            break
    player_two_mark = 'O' if player_one_mark == 'X' else 'X'
    print(f'Player 1 will play with {player_one_mark}, Player 2 will play with {player_two_mark}.')
    return player_one_mark, player_two_mark


def print_initial_board():
    initial_board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print('-TIC-TAK-TOE-')
    for row in initial_board:
        print('| ', end='')
        print(' | '.join(list(map(str, row))), end='')
        print(' |')
    print()
    print('This is the numeration of the board.\nRemember it and play!')
    print()


def print_current_board(board):
    print('-TIC-TAK-TOE-')
    for row in board:
        print('| ', end='')
        print(' | '.join(list(map(str, row))), end='')
        print(' |')
    print()


def get_move(matrix, current_player, current_mark):

    positions = {
        '1': [0, 0],
        '2': [0, 1],
        '3': [0, 2],
        '4': [1, 0],
        '5': [1, 1],
        '6': [1, 2],
        '7': [2, 0],
        '8': [2, 1],
        '9': [2, 2]
    }

    while True:
        move = input(f'{current_player}, please choose a FREE position from 1 to 9: ')
        if move not in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            print('Please try again!')
            continue
        row = positions[move][0]
        col = positions[move][1]
        if matrix[row][col] != ' ':
            print('Position taken!')
            continue
        matrix[row][col] = current_mark
        return matrix, row, col


def is_draw(board):
    for r in board:
        for el in r:
            if el == ' ':
                return False
    print('Draw! Try again!')
    return True


def is_winning(matrix, player_mark, player):
    current = player_mark
    first_row = all([x == current for x in matrix[0]])
    second_row = all([x == current for x in matrix[1]])
    third_row = all([x == current for x in matrix[2]])
    first_column = all([x == current for x in [matrix[0][0], matrix[1][0], matrix[2][0]]])
    second_column = all([x == current for x in [matrix[0][1], matrix[1][1], matrix[2][1]]])
    third_column = all([x == current for x in [matrix[0][2], matrix[1][2], matrix[2][2]]])
    first_diagonal = all([x == current for x in [matrix[0][0], matrix[1][1], matrix[2][2]]])
    second_diagonal = all([x == current for x in [matrix[0][2], matrix[1][1], matrix[2][0]]])

    if any((first_row, second_row, third_row, first_column, second_column, third_column, first_diagonal, second_diagonal)):
        print(f'{player} won!')
        return True
    return False


player_one = input('Player one name: ')
player_two = input('Player two name: ')

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

current_player = player_one
other_player = player_two


player_one_mark, player_two_mark = get_started(player_one)

current_mark = player_one_mark
other_mark = player_two_mark

print("Let's start the game!")
print()
print_initial_board()


while True:
    board, row, col = get_move(board, current_player, current_mark)
    print_current_board(board)
    if is_draw(board):
        break
    if is_winning(board, current_mark, current_player):
        break
    current_player, other_player = other_player, current_player
    current_mark, other_mark = other_mark, current_mark
