from collections import deque

def is_inside(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True
    return False


size = 6
matrix = []
directions = {"up": (-1, 0),
              "down":(1, 0)}
for _ in range(size):
    rows = [x for x in input().split()]
    matrix.append(rows)

coordinates = deque([])

for i in range(3):
    row, col = eval(input())
    coordinates.append((int(row), int(col)))

sum_of_col = 0

while coordinates:
    current_row, current_col = coordinates.popleft()
    if is_inside(current_row, current_col, size):
        if matrix[current_row][current_col] == "B":
            for direction in directions:
                new_row = current_row + directions[direction][0]
                new_col = current_col + directions[direction][1]
                while is_inside(new_row, new_col, size):
                    new_el = int(matrix[new_row][new_col])
                    sum_of_col += new_el
                    new_row += directions[direction][0]
                    new_col += directions[direction][1]
            matrix[current_row][current_col] = '0'

prize = ""
if 100 <= sum_of_col <= 199:
    prize = 'Football'
elif 200 <= sum_of_col <= 299:
    prize = "Teddy Bear"
elif sum_of_col >= 300:
    prize = "Lego Construction Set"

if prize:
    print(f"Good job! You scored {sum_of_col} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - sum_of_col} points more to win a prize.")