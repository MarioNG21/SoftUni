from collections import deque


def is_inside(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def new_matrix(r, c, matrix):
    if matrix[r][c] > 0:
        explosion = matrix[r][c]
        matrix[r][c] = 0
        if is_inside(r - 1, c, len(matrix)):
            if matrix[r - 1][c] > 0:
                matrix[r - 1][c] -= explosion

        if is_inside(r + 1, c, len(matrix)):
            if matrix[r + 1][c] > 0:
                matrix[r + 1][c] -= explosion

        if is_inside(r, c - 1, len(matrix)):
            if matrix[r][c - 1] > 0:
                matrix[r][c - 1] -= explosion

        if is_inside(r, c + 1, len(matrix)):
            if matrix[r][c + 1] > 0:
                matrix[r][c + 1] -= explosion

        if is_inside(r - 1, c - 1, len(matrix)):
            if matrix[r - 1][c - 1] > 0:
                matrix[r - 1][c - 1] -= explosion

        if is_inside(r - 1, c + 1, len(matrix)):
            if matrix[r - 1][c + 1] > 0:
                matrix[r - 1][c + 1] -= explosion

        if is_inside(r + 1, c - 1, len(matrix)):
            if matrix[r + 1][c - 1] > 0:
                matrix[r + 1][c - 1] -= explosion

        if is_inside(r + 1, c + 1, len(matrix)):
            if matrix[r + 1][c + 1] > 0:
                matrix[r + 1][c + 1] -= explosion

    return matrix


size = int(input())
matrix = []
bomb_coordinates = deque()
for row in range(size):
    rows = [int(x) for x in input().split()]
    matrix.append(rows)

for group in input().split():
    r, c = group.split(',')
    bomb_coordinates.append((int(r), int(c)))

while bomb_coordinates:
    current_bomb = bomb_coordinates.popleft()
    current_row, current_col = current_bomb
    matrix_2 = new_matrix(current_row, current_col, matrix)
    matrix = matrix_2

sum_of_alive = 0
counter = 0
for n in range(size):
    for m in range(size):
        if matrix[n][m] > 0:
            counter += 1
            sum_of_alive += matrix[n][m]

print(f"Alive cells: {counter}")
print(f"Sum: {sum_of_alive}")

for j in matrix:
    print(' '.join([str(x) for x in j]))

