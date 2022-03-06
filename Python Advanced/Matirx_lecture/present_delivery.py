def is_inside(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def get_houses_in_range(r, c, size):
    houses = []
    if is_inside(next_santa_row - 1, next_santa_clm, size):
        houses.append([r - 1, c])
    if is_inside(next_santa_row + 1, next_santa_clm, size):
        houses.append([r + 1, c])
    if is_inside(next_santa_row, next_santa_clm - 1, size):
        houses.append([r, c - 1])
    if is_inside(next_santa_row, next_santa_clm + 1, size):
        houses.append([r, c + 1])

    return houses


def get_direction(direction, r, c):
    if direction == "up":
        return r - 1, c
    if direction == "down":
        return r + 1, c
    if direction == "left":
        return r, c - 1
    return r, c + 1


number_of_presents = int(input())

size = int(input())

matrix = []
santa_row, santa_clm = 0, 0
nice_kids_counter = 0


for r in range(size):
    rows = input().split()
    matrix.append(rows)
    for c in range(size):
        if rows[c] == "S":
            santa_row, santa_clm = r, c
        elif rows[c] == "V":
            nice_kids_counter += 1
left = nice_kids_counter

while True:
    command = input()
    if command == "Christmas morning":
        break
    next_santa_row, next_santa_clm = get_direction(command, santa_row, santa_clm)

    if matrix[next_santa_row][next_santa_clm] == "X":
        matrix[next_santa_row][next_santa_clm] = "-"

    elif matrix[next_santa_row][next_santa_clm] == "V":
        number_of_presents -= 1
        nice_kids_counter -= 1
        matrix[next_santa_row][next_santa_clm] = "-"

    elif matrix[next_santa_row][next_santa_clm] == "C":
        houses_in_range = get_houses_in_range(next_santa_row, next_santa_clm, size)
        for row, col in houses_in_range:
            if matrix[row][col] == "X":
                number_of_presents -= 1
            if matrix[row][col] == "V":
                number_of_presents -= 1
                nice_kids_counter -= 1
            matrix[row][col] = "-"
            if number_of_presents == 0:
                break

    matrix[santa_row][santa_clm] = "-"
    matrix[next_santa_row][next_santa_clm] = "S"
    santa_row, santa_clm = next_santa_row, next_santa_clm
    if number_of_presents == 0:
        break

if number_of_presents <= 0 and nice_kids_counter > 0 :
    print("Santa ran out of presents!")
for _ in matrix:
    print(' '.join(_))

if nice_kids_counter <= 0:
    print(f"Good job, Santa! {left} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_counter} nice kid/s.")