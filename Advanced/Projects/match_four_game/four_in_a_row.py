from datetime import datetime


class InvalidColumnError(Exception):
    pass


class ColumnIsFullError(Exception):
    pass


# print the field
def print_matrix(ma):
    print(' ---Current Field---')
    for el in ma:
        print(el)


# validating input is in the matrix
def validate_column_choice(selected_column_num, max_column_index):
    if not (0 <= selected_column_num <= max_column_index):
        raise InvalidColumnError


def place_player_choice_on_field(ma, column_index, player):
    rows = len(ma)
    for row_index in range(rows-1, -1, -1):
        current_element = ma[row_index][column_index]
        if current_element == 0:
            ma[row_index][column_index] = player
            return row_index, column_index
    else:
        raise ColumnIsFullError


def is_player_num(ma, row, col, player):
    if col < 0 or row < 0:
        return False
    try:
        if ma[row][col] == player:
            return True
    except IndexError:
        return False
    return False


def is_horizontal(ma, row, col, player, slots_count):
    right = []
    for index in range(slots_count):
        if is_player_num(ma, row, col + index, player):
            right.append(True)
        else:
            break
    left = []
    for index in range(slots_count):
        if is_player_num(ma, row, col - index, player):
            left.append(True)
        else:
            break

    return len(right + left) > slots_count


def is_right_diagonal(ma, row, col, player, slots_count):
    count_right_up = [is_player_num(ma, row - index, col + index, player) for index in range(slots_count)].count(True)
    count_left_down = [is_player_num(ma, row + index, col - index, player) for index in range(slots_count)].count(True)
    return (count_right_up + count_left_down) > slots_count


def is_left_diagonal(ma, row, col, player, slots_count):
    count_left_up = [is_player_num(ma, row - index, col - index, player) for index in range(slots_count)].count(True)
    count_right_down = [is_player_num(ma, row + index, col + index, player) for index in range(slots_count)].count(True)
    return (count_left_up + count_right_down) > slots_count


# Winning condition here, works with all the verifications above - left diagonal, right diagonal and horizontal
def is_winner(ma, row, col, player, slots_count=4):
    up = all([is_player_num(ma, row - index, col, player) for index in range(slots_count)])
    down = all([is_player_num(ma, row + index, col, player) for index in range(slots_count)])

    is_horizontal(ma, row, col, player, slots_count=4)
    if any(
            (
                    is_horizontal(ma, row, col, player, slots_count=4),
                    is_right_diagonal(ma, row, col, player, slots_count=4),
                    is_left_diagonal(ma, row, col, player, slots_count=4),
                    up,
                    down,
            )
    ):
        return True
    return False


# field size
rows_count = 6
cols_count = 7
game_counter = 0

# Generating the field
matrix = [[0 for _ in range(cols_count)] for row_num in range(rows_count)]

print_matrix(matrix)

player_num = 1

while True:
    # read column choice from input to start playing the game
    try:
        player_num = 2 if player_num % 2 == 0 else 1
        column_num = int(input(f'Player {player_num}, please choose a column: ')) - 1
        # validating
        validate_column_choice(column_num, cols_count - 1)
        current_row, current_col = place_player_choice_on_field(matrix, column_num, player_num)
        if is_winner(matrix, current_row, current_col, player_num):
            print_matrix(matrix)
            print('---------------------')
            print(f'   Player {player_num} wins!')
            print('---------------------')
            game_counter += 1
            break
        print_matrix(matrix)

    except InvalidColumnError:
        print(f'That is not a valid column number! Please select a number between {1} and {cols_count}')
        continue
    except ValueError:
        print('This is not a number! Please choose a valid number!')
        continue
    except ColumnIsFullError:
        print('This column is full! Please pick another one!')
        continue
    player_num += 1


with open('results_log.txt', 'a') as file:
    file.write('--------------------------------\n')
    file.write(f'Time: {datetime.now()}\n')
    file.write(f'Game {game_counter} - winner is Player {player_num}\n')
    file.write('--------------------------------\n')
