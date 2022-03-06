def is_valid(r, c, size):
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
alice_row = 0
alice_col = 0
collected_tea = 0

for row in range(size):
    rows = [x for x in input().split()]
    matrix.append(rows)
    for col in range(size):
        if matrix[row][col] == "A":
            alice_row, alice_col = row, col
matrix[alice_row][alice_col] = "*"
has_tea_party = False

while True:
    command = input()
    if command == '':
        break
    next_row, next_col = moving(alice_row, alice_col, command)
    if is_valid(next_row, next_col, size):
        new_el = matrix[next_row][next_col]
        if new_el == "R":
            matrix[next_row][next_col] = '*'
            break
        elif new_el.isdigit():
            collected_tea += int(new_el)
            if collected_tea >= 10:
                has_tea_party = True
                matrix[next_row][next_col] = '*'
                break
        alice_row, alice_col = next_row, next_col
        matrix[alice_row][alice_col] = '*'

    else:
        break

if not has_tea_party:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for j in matrix:
    print(' '.join(j))