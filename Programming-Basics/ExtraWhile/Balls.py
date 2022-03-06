# червената е + 5
# оранджевата е + 10
# жълтата е с + 15
# бялата е с + 20
#  черната е делене на 2 и закръгляне към по-малкото
from math import floor
number_of_balls = int(input())
sum_of_points = 0
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
other_balls = 0
for balls in range(1, number_of_balls+1):
    colour_of_balls = input()
    if colour_of_balls == "red":
        sum_of_points += 5
        red_balls += 1
    elif colour_of_balls == "orange":
        sum_of_points += 10
        orange_balls += 1
    elif colour_of_balls == "yellow":
        sum_of_points += 15
        yellow_balls += 1
    elif colour_of_balls == "white":
        sum_of_points += 20
        white_balls += 1
    elif colour_of_balls == "black":
        sum_of_points = floor(sum_of_points / 2)
        balls += 1
    else:
        sum_of_points += 0
        other_balls += 1
print(f"Total points: {sum_of_points}")
print(f"Points from red balls: {red_balls}")
print(f"Points from orange balls: {orange_balls}")
print(f"Points from yellow balls: {yellow_balls}")
print(f"Points from white balls: {white_balls}")
print(f"Other colors picked: {other_balls}")
print(f"Divides from black balls: {black_balls}")
