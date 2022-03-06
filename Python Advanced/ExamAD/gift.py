def get_turn():
    turn_string = input()
    vals = turn_string[1:-1].split(', ')
    return [int(val) for val in vals]
 
def get_value(board, row_index, column_index):
    value = board[row_index][column_index]
    points = 0
    if value == "B":
        for i in range(6):
            point = board[int(i)][column_index]
            if point.isnumeric():
                points += int(point)
        board[row_index][column_index] = '0'

    return points

def in_range(val, max_value):
    if 0 <= val < max_value:
        return True
    return False

def win(current):
    if 100 <= current <= 199:
        return f"Good job! You scored {current} points, and you've won Football."
    elif 200 <= current <= 299:
        return f"Good job! You scored {current} points, and you've won Teddy Bear."
    elif current >= 300:
        return f"Good job! You scored {current} points, and you've won Lego Construction Set."
    else:
        return f"Sorry! You need {100 - current} points more to win a prize."
def solve(board):
    current = 0
    for turn in range(3):
        (row_index, colulmn_index) = get_turn()
        if not in_range(row_index, n) and not in_range(colulmn_index, m):
            continue
        value = get_value(board, row_index, colulmn_index)
        current += value
    return win(current)
 
my_dict = {}
n = 6
m = 6
board = [input().split() for _ in range(n)]
print(solve(board))