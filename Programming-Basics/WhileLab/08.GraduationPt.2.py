name = input()
fail = 0
has_failed = True
grade = 0
sum_of_score = 0
years = 0

while fail <= 1:
    overall_score = float(input())
    if overall_score < 4.00:
        fail += 1
    if fail > 1:
        has_failed = False
        break
    grade += 1
    sum_of_score += overall_score
    years += 1
if has_failed == False :
    print(f"{name} has been excluded at {grade} grade")
else:
    print(f"{name} graduated. Average grade: {sum_of_score/years:.2f}")