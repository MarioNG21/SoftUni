from collections import deque

rows = int(input())
matrix = []
bomb_coordinates = deque()

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

command = input().split()

for _ in range(len(command)):
    cmd_arg = command[_].split(',')
    r, c = int(cmd_arg[0]), int(cmd_arg[1])
    bomb_coordinates.append((r, c))

counter = 0
sum_overall = 0
while bomb_coordinates:
    row, clm = bomb_coordinates.popleft()
    bomb = matrix[row][clm]
    if bomb <= 0:
        continue
    for r in range(rows):
        for c in range(rows):
            if (r == row - 1 and clm - 1 <= c <= clm + 1) or (r == row and clm - 1 <= c <= clm + 1) or \
                    (r == row + 1 and clm - 1 <= c <= clm + 1):
                if matrix[r][c] > 0:
                    matrix[r][c] -= bomb

for i in range(len(matrix)):
    small_matrix = matrix[i]
    for j in range(len(small_matrix)):
        if small_matrix[j] > 0:
            counter += 1
            sum_overall += small_matrix[j]

print(f"Alive cells: {counter}")
print(f"Sum: {sum_overall}")
for _ in matrix:
    print(' '.join(str(x) for x in _))















    # for _ in range(rows - 1):
    #     matrix[row][clm - 1] -= bomb
    #     matrix[row][clm + 1] -= bomb
    #     matrix[row - 1][clm] -= bomb
    #     matrix[row + 1][clm] -= bomb
    #     matrix[row - 1][clm - 1] -= bomb
    #     matrix[row - 1][clm + 1] -= bomb
    #     matrix[row - 1][clm - 1] -= bomb
    #     matrix[row + 1][clm - 1] -= bomb
    #     matrix[row + 1][clm + 1] -= bomb