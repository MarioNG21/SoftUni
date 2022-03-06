def is_outside(r, c, size):
    if r < 0 or c < 0 or r >= size or c >= size:
        return True
    return False


def get_next_position(direction, r, c):
    if direction == 'up':
        return r - 1, c
    if direction == "down":
        return r + 1, c
    if direction == "left":
        return r, c - 1
    return r, c + 1


size = int(input())

matrix = []

alice_row, alice_col = 0, 0
for row in range(size):
    elements = input().split()
    matrix.append(elements)
    for col in range(size):
        element = elements[col]
        if element == "A":
            alice_row, alice_col = row, col


tea_bags = 0
matrix[alice_row][alice_col] = "*"
while True:
    command = input()
    alice_row, alice_col = get_next_position(command, alice_row, alice_col)
    cell_value = matrix[alice_row][alice_col]
    if is_outside(alice_row, alice_col, size):
        break
    matrix[alice_row][alice_col] = '*'
    if cell_value == "R":
        break
    elif cell_value.isdigit():
        tea_bags += int(cell_value)
        if tea_bags >= 10:
            break


if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(' '.join(row))