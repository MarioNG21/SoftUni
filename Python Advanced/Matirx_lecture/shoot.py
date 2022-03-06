def is_outside(row, col, size):
    if row < 0 or col < 0 or row >= size or col >= size:
        return True
    return False


def get_next_position(direction, r, c, step):
    if direction == 'up':
        return r - step, c
    if direction == "down":
        return r + step, c
    if direction == "left":
        return r, c - step
    return r, c + step


size = 5

matrix = []

player_row, player_col = 0, 0
target_count = 0
for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == "A":
            player_row, player_col = row, col
        elif element == "x":
            target_count += 1


shooting_directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

counter = []

n = int(input())
for _ in range(n):
    line_args = input().split()
    command = line_args[0]
    direction = line_args[1]
    if command == "move":
        steps = int(line_args[2])
        next_player_row, next_player_col = get_next_position(direction, player_row, player_col, steps)

        if is_outside(next_player_row, next_player_col, size):
            continue

        if matrix[next_player_row][next_player_col] != '.':
            continue

        matrix[player_row][player_col] = '.'
        matrix[next_player_row][next_player_col] = 'A'
        player_row, player_col = next_player_row, next_player_col
    else:
        step = shooting_directions[direction]
        bullet_row, bullet_col = step(player_row, player_col)
        while True:
            if is_outside(bullet_row, bullet_col, size):
                break
            if matrix[bullet_row][bullet_col] == 'x':
                counter.append([bullet_row, bullet_col])
                matrix[bullet_row][bullet_col] = '.'
                break
            bullet_row, bullet_col = step(bullet_row, bullet_col)
        if len(counter) == target_count:
            break


if len(counter) == target_count:
    print(f"Training completed! All {len(counter)} targets hit.")
else:
    print(f"Training not completed! {target_count - len(counter)} targets left.")

for target in counter:
    print(target)