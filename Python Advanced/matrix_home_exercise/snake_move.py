rows, cols = (int(x) for x in input().split())
matrix = []
snake_str = input()

for _ in range(rows):
    matrix.append([None] * cols)


word_idx = 0
for row in range(rows):
    for col in range(cols):
        if row % 2 == 0:
            matrix[row][col] = snake_str[(word_idx ) % len(snake_str)]
        else:
            matrix[row][cols - col - 1] = snake_str[(word_idx ) % len(snake_str)]
        word_idx += 1

for j in matrix:
    print(''.join(j))