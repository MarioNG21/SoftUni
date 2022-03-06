n = int(input())

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split()]
    matrix.append(row)

m = len(matrix[0])
value = 0
for r in range(n):
    for c in range(m):
        if c == r:
            value += matrix[r][c]

print(value)
