def is_inside(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def moving(r, c, direction):
    if direction == "up":
        return r - 1, c
    elif direction == "down":
        return r + 1, c
    elif direction == "left":
        return r, c - 1
    return r, c + 1


size = int(input())
matrix = []

snake_row, snake_col = 0, 0
holes_coordinates = []
for _ in range(size):
    rows = list(input())
    matrix.append(rows)
    for c in range(size):
        if matrix[_][c] == "S":
            snake_row, snake_col = _, c
        if matrix[_][c] == "B":
            holes_coordinates.append([_, c])

went_outside = False
eat_all = False
matrix[snake_row][snake_col] = '.'
food_qnt = 0
while True:
    command = input()
    if command == "":
        break
    next_row, next_col = moving(snake_row, snake_col, command)
    if is_inside(next_row, next_col, size):
        el = matrix[next_row][next_col]
        if el == "*":
            food_qnt += 1
            if food_qnt >= 10:
                eat_all = True
                matrix[next_row][next_col] = "."
                snake_row, snake_col = next_row, next_col
                break
        elif el == "B":
            holes_coordinates.remove([next_row, next_col])
            matrix[next_row][next_col] = "."
            next_row, next_col = holes_coordinates.pop()
        matrix[next_row][next_col] = "."
        snake_row, snake_col = next_row, next_col

    else:
        went_outside = True
        break

if not went_outside:
    matrix[snake_row][snake_col] = "S"
if went_outside:
    print("Game over!")
if eat_all:
    print("You won! You fed the snake.")
print(f"Food eaten: {food_qnt}")
for j in matrix:
    print(''.join(j))
