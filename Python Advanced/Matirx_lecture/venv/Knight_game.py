def is_knight_placed(board, row, col):
    if row < 0 or col < 0 or row >= len(board) or col >= len(board):
        return False
    return board[row][col] == "K"

def count_affected_knights(board, row, cl):
    result = 0
    board_size = len(board)
    if is_knight_placed(board, row - 2, cl - 1):
        result += 1
    if is_knight_placed(board, row - 2, cl + 1):
        result += 1
    if is_knight_placed(board, row + 2, cl - 1):
        result += 1
    if is_knight_placed(board, row + 2, cl + 1):
        result += 1
    if is_knight_placed(board, row - 1, cl - 2):
        result += 1
    if is_knight_placed(board, row - 1, cl + 2):
        result += 1
    if is_knight_placed(board, row + 1, cl + 2):
        result += 1
    if is_knight_placed(board, row + 1, cl - 2):
        result += 1
    return result
size = int(input())

matrix = []
removed_knights = 0


for _ in range(size):
    matrix.append(list(input()))

while True:
    max_count, knight_row, knight_col = 0, 0, 0
    for r in range(size):
        for c in range(size):
            if matrix[r][c] == "0":
                continue
            else:
                count = count_affected_knights(matrix, r, c)
                if count > max_count:
                    max_count, knight_row, knight_col = count, r, c
    if max_count == 0:
        break
    matrix[knight_row][knight_col] = "0"
    removed_knights += 1
print(removed_knights)