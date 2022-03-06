from math import floor
income = float(input())
marks = float(input())
minimal_wage = float(input())


if income > minimal_wage and marks <= 4.5 or marks < 5.5:
    print(f"You cannot get a scholarship!")
if income < minimal_wage and marks > 4.5:
    social_scholarship = 0.35 * minimal_wage
    print(f"You get a Social scholarship {floor(social_scholarship)} BGN")
if marks >= 5.5:
    scholarship_for_grades = 25 * marks
    print(f"You get a scholarship for excellent results {floor(scholarship_for_grades)} BGN")
if income < minimal_wage:
    if marks > 4.5:
        social_scholarship = 0.35 * minimal_wage
    else marks >= 5.5:
        scholarship_for_grades = 25 * marks
        if social_scholarship > scholarship_for_grades:
            print(floor(social_scholarship))
        elif social_scholarship <= scholarship_for_grades:
            print(floor(scholarship_for_grades))





