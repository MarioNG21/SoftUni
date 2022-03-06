def is_invalid_position(r, c, size):
    if row < 0 or col < 0 or r >= size or c >= size:
        return True
size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

while True:
    line = input()
    if line == "END":
        break

    args = line.split()
    command = args[0]
    row, col, value = [int(x) for x in args[1:]]
    if is_invalid_position(row, col, size):
        print("Invalid coordinates")
        continue
    if command == "Add":
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

for row_el in matrix:
    print(' '.join([str(x) for x in row_el]))
