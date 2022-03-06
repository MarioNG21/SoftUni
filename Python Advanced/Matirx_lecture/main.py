def are_valid(r, c, rows, cols):
    if r < 0 or c < 0 or r >= rows or c >= cols:
        return False
    return True


n, m = [int(x) for x in input().split()]

matrix = []

for _ in range(n):
    matrix.append([x for x in input().split()])

while True:
    line = input()
    if line == "END":
        break
    args = line.split()
    if args[0] != "swap" or len(args) > 5:
        print("Invalid input!")
        line = input()
        continue
    row1 = int(args[1])
    col1 = int(args[2])
    row2 = int(args[3])
    col2 = int(args[4])

    if are_valid(row1, col1, n, m) and are_valid(row2, col2, n, m):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for r in range(len(matrix)):
            r = matrix[r]
            print(*r)
    else:
        print("Invalid input!")
