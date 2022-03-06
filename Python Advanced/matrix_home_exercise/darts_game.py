def score_counter(matrix, c, r):
    score = 0
    counter = 0
    score += int(matrix[r][0])
    score += int(matrix[r][-1])
    score += int(matrix[0][c])
    score += int(matrix[-1][c])
    return score


def valid_idx(r, c, board):
    if 0 <= r < board and 0 <= c < board:
        return True
    return False


first_player_points, second_player_points = 501, 501

size = 7
first_player, second_player = input().split(', ')
count = 0

first_player_won = False
second_player_won = False

first_player_shots = 0
second_player_shots = 0


still_playing = True

matrix = []

for _ in range(size):
    rows = input().split()
    matrix.append(rows)


while still_playing:
    current_cord = input()
    current_row, current_clm = eval(current_cord)
    points = 0
    if valid_idx(current_row, current_clm, size):
        el = matrix[current_row][current_clm]
        if el.isdigit():
            points += int(el)
        elif el == 'D':
            points = score_counter(matrix, current_clm, current_row) * 2
        elif el == 'T':
            points = score_counter(matrix, current_clm, current_row) * 3
        elif el == 'B':
            if count % 2 == 0:
                first_player_won = True
                still_playing = False
            elif count % 2 != 0:
                second_player_won = True
                still_playing = False

        if count % 2 == 0:
            first_player_points -= points
            first_player_shots += 1
            if first_player_points <= 0:
                first_player_won = True
                still_playing = False
                break

        elif count % 2 == 1:
            second_player_points -= points
            second_player_shots += 1
            if second_player_points <= 0:
                second_player_won = True
                still_playing = False
                break

        count += 1

    else:
        if count % 2 == 0:
            first_player_shots += 1
        elif count % 2 != 0:
            second_player_shots += 1
        count += 1
        continue

if first_player_won:
    print(f"{first_player} won the game with {first_player_shots} throws!")
else:
    print(f"{second_player} won the game with {second_player_shots} throws!")