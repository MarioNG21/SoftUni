from sys import maxsize


def is_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


size = int(input())

direction = {'up': (-1, 0),
             'down': (1, 0),
             'left': (0, -1),
             'right': (0, 1)
             }

most_eggs = []
max_eggs = - maxsize
best_coordinates = {}

matrix = []

bunny_row, bunny_col = 0, 0
for row in range(size):
    rows = [x for x in input().split()]
    matrix.append(rows)
    for col in range(size):
        if matrix[row][col] == "B":
            bunny_row, bunny_col = row, col

for key in direction:
    start_row = bunny_row + direction[key][0]
    start_col = bunny_col + direction[key][1]
    egg_counter = 0
    egg_path = []
    found_trap = False
    if is_valid(start_row, start_col, size):
        while is_valid(start_row, start_col, size):
            was_inside = True
            if matrix[start_row][start_col] == "X":
                break
            egg_path.append([start_row, start_col])
            egg_counter += int(matrix[start_row][start_col])
            start_row += direction[key][0]
            start_col += direction[key][1]
        best_coordinates[key] = [egg_path, egg_counter]
    else:
        continue
for key, value in sorted(best_coordinates.items(), key=lambda kvp: -kvp[1][1]):
    print(key.lower())
    for cor in value[0]:
        print(cor)
    print(value[1])
    break