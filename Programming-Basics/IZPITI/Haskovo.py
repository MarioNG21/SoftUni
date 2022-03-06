from math import  floor
number_of_tournaments = int(input())
start_points = int(input())
win_counter = 0
average_points = 0
for matches in range(1, number_of_tournaments+1):
    stage = input()
    if stage == "W":
        start_points += 2000
        average_points += 2000
        win_counter += 1
    elif stage == "F":
        start_points += 1200
        average_points += 1200
    else:
        start_points += 720
        average_points += 720
average_points = average_points / number_of_tournaments
print(f"Final points: {start_points}")
print(f"Average points: {floor(average_points)}")
print(f"{(win_counter/number_of_tournaments) * 100:.2f}%")