matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]
          ]


above_primary_diagonal = []

n = len(matrix)
m = len(matrix[0])
#for r in range(n):
#    for c in range(r+1, n):
#        above_primary_diagonal.append(matrix[r][c])


below_primary = []

#for r in range(n):
#    for c in range(r):
#        below_primary.append(matrix[r][c])

secondary_diagonal = []

#for r in range(n):
#    secondary_diagonal.append(matrix[r][m - r - 1])

above_secondary = []

for r in range(n):
    for c in range(n - r - 1):
        above_secondary.append(matrix[r][c])

below_secondary = []

for row in range(n):
    for column in range(n - row, n):
        below_secondary.append(matrix[row][column])
