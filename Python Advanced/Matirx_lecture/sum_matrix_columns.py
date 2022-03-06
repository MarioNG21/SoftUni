n, m = [int(x) for x in input().split(', ')]

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)


n = len(matrix)
m = len(matrix[0])

column_sums = [0] * m

for r in range(n):
    for c in range(m):
        value = matrix[r][c]
        column_sums[c] += value

# създава една матрица която репрезентира само колоните и вървим ред по ред и гледам за едната и съща позиция какви елементи е ималко на всеки един ред и го добавя например на ред 1 на колонка едно е имало 5 и след това на ред 2 на колонка 1 е имало 5 и резулатата става 10

for _ in column_sums:
    print(_)