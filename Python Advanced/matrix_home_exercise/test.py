size = 8

matrix = []


for _ in range(size):
    rows = list(input().split())
    matrix.append(rows)

directions = {'up': (-1, 0),
              'down': (1, 0),
              'left': (0, -1),
              'right': (0, 1),
              'up_left': (-1, -1),
              'up_right': (-1, 1),
              'down_left': (1, -1),
              'down_right': (1, 1)
              }


def is_inside(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


coordinates_of_queen = []
for row in range(size):
    for col in range(size):
        if matrix[row][col] == "Q":
            for direction in directions:
                next_row = row + directions[direction][0]
                next_col = col + directions[direction][1]
                while is_inside(next_row, next_col, size):
                    if matrix[next_row][next_col] == "Q":
                        break
                    if matrix[next_row][next_col] == "K":
                        coordinates_of_queen.append([row, col])
                    next_row += directions[direction][0]
                    next_col += directions[direction][1]

if coordinates_of_queen:
    for el in coordinates_of_queen:
        print(el)
else:
    print("The king is safe!")
