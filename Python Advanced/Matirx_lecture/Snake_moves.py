rows, cols = [int(x) for x in input().split()]
word = input()
matrix = []
word_index = 0
for r in range(rows):
    matrix.append([None] * cols)
    for col in range(cols):
        if r % 2 == 0:
            matrix[r][col] = word[word_index]
        else:
            matrix[r][cols - 1 - col] = word[word_index]

        word_index = (word_index + 1) % len(word)

for elements in matrix:
    print(''.join(elements))