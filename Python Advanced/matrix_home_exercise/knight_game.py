from sys import maxsize


def valid_move(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


def knight_move(r, c, matrix, count=0):

    if valid_move(r - 2, c - 1, size):
        if matrix[r - 2][c - 1] == "K":
            count += 1

    if valid_move(r - 2, c + 1, size):
        if matrix[r - 2][c + 1] == "K":
            count += 1

    if valid_move(r - 1, c - 2, size):
        if matrix[r - 1][c - 2] == "K":
            count += 1

    if valid_move(r - 1, c + 2, size):
        if matrix[r - 1][c + 2] == "K":
            count += 1

    if valid_move(r + 1, c - 2, size):

        if matrix[r + 1][c - 2] == "K":
            count += 1
    if valid_move(r + 1, c + 2, size):
        if matrix[r + 1][c + 2] == "K":
            count += 1

    if valid_move(r + 2, c - 1, size):
        if matrix[r + 2][c - 1] == "K":
            count += 1

    if valid_move(r + 2, c + 1, size):
        if matrix[r + 2][c + 1] == "K":
            count += 1

    return count


size = int(input())

matrix = []
count = 0


for _ in range(size):
    matrix.append([x for x in input()])

removed_knights = 0
while True:
    max_count = - maxsize
    knight_row, knight_clm = 0, 0
    for row in range(size):
        for clm in range(size):
            el = matrix[row][clm]
            if el == "K":
                count = knight_move(row, clm, matrix)
                if count > max_count:
                    knight_row, knight_clm = row, clm
                    max_count = count
    if max_count == 0:
        break
    
    matrix[knight_row][knight_clm] = '0'
    removed_knights += 1

print(removed_knights)