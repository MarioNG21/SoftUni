from collections import deque


def is_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def moving(row, clm, d):
    if is_valid(row, clm - 1, size) and d == 'left':
        return row, clm - 1
    elif is_valid(row, clm + 1, size) and d == 'right':
        return row, clm + 1
    elif is_valid(row - 1, clm, size) and d == 'up':
        return row - 1, clm
    elif is_valid(row + 1, clm, size) and d == 'down':
        return row + 1, clm
    else:
        return row, clm


size = int(input())
directions = deque(input().split())
matrix = []

miner_row, miner_clm = 0, 0

coal_in_mine = 0

for r in range(size):
    rows = [x for x in input().split()]
    matrix.append(rows)
    for c in range(size):
        if matrix[r][c] == 's':
            miner_row, miner_clm = r, c
        elif matrix[r][c] == 'c':
            coal_in_mine += 1
current_row, current_clm = miner_row, miner_clm
while coal_in_mine:
    if not directions and coal_in_mine:
        print(f"{coal_in_mine} pieces of coal left. ({current_row}, {current_clm})")
        break
    current_direction = directions.popleft()
    new_row, new_clm = moving(current_row, current_clm, current_direction)

    if new_row == current_row and new_clm == current_clm:
        continue

    if matrix[new_row][new_clm] == 'c':
        coal_in_mine -= 1
        matrix[new_row][new_clm] = '*'
        if coal_in_mine <= 0:
            miner_row, miner_clm = new_row, new_clm
            break

    if matrix[new_row][new_clm] == 'e':
        print(f'Game over! ({new_row}, {new_clm})')
        break

    matrix[current_row][current_clm] = '*'
    matrix[new_row][new_clm] = 's'
    current_row, current_clm = new_row, new_clm

if not coal_in_mine:
    print(f"You collected all coal! ({miner_row}, {miner_clm})")