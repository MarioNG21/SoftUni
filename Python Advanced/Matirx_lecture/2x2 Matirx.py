rows, columns = [int(x) for x in input().split()]

matrix = []
for _ in range(rows):
    row = [x for x in input().split()]
    matrix.append(row)

counter = 0
for r in range(rows - 1):
    for c in range(columns - 1):
        first_pair = matrix[r][c] + matrix[r][c + 1]
        second_pair = matrix[r + 1][c] + matrix[r + 1][c + 1]
        if first_pair == second_pair and matrix[r][c] == matrix[r][c + 1] :
            counter += 1

print(counter)