def is_valid_index(r, c , rows, columns):
    if 0 <= r < rows and 0 <= c < columns:
        return True
    return False


rows, clm = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split()])

command = input()
while command != "END":
    cmd_arg = command.split()
    if cmd_arg[0] != 'swap' or len(cmd_arg) > 5:
        print('Invalid input!')
        command = input()
        continue
    row1 = int(cmd_arg[1])
    col1 = int(cmd_arg[2])
    row2 = int(cmd_arg[3])
    col2 = int(cmd_arg[4])

    if not is_valid_index(row1, col1, rows, clm) or not is_valid_index(row2, col2, rows, clm):
        print('Invalid input!')

    else:
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for r in range(len(matrix)):
            r = matrix[r]
            print(*r)

    command = input()
