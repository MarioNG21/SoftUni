matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

n = 5
# primary
print(
    [matrix[i][i] for i in range(n)]
)
#secondary
print(
    [matrix[x][n - 1-x] for x in range(n)]
)