rows, cols = (int(x) for x in input().split())

matrix = []
ascii_chr = 97
for row in range(rows):
    matrix.append([None] * cols)
    for col in range(cols):
        first_chr = chr(ascii_chr + row)
        middle = chr(ascii_chr + row + col)
        last_chr = chr(ascii_chr + row)
        word = first_chr + middle + last_chr
        matrix[row][col] = word

for j in matrix:
    print(' '.join(j))