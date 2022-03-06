from sys import maxsize
from math import ceil


def bonus_calculation(student_attendances: int, number_lectures: int, bonus_points: int):
    total_bonus = (student_attendances / number_lectures) * (5 + bonus_points)
    return total_bonus


counter_for_students = int(input())
counter_for_lectures = int(input())
bonus = int(input())
winner_score = 0
winner = 0
while counter_for_students > 0:
    max_score = - maxsize
    winners_attendance = 0
    for student in range(1, counter_for_students+1):
        attendances = int(input())
        personal_points = bonus_calculation(attendances, counter_for_lectures, bonus)
        if personal_points > max_score:
            max_score = personal_points
            winners_attendance = attendances
        counter_for_students -= 1
    winner_score = max_score
    winner = winners_attendance


print(f"Max Bonus: {ceil(winner_score)}.")
print(f"The student has attended {winner} lectures.")
