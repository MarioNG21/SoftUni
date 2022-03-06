count_jury = int(input())
presentation = input()
sum_all_grades = 0
count = 0
# stop: presentation == "Finish"
# continue: presentation != "Finish"
while presentation != "Finish":
    # за всяка една презентация: четем по една оценка от всеки от журито
    sum_grades = 0 #  занулява се за вска една презентация и е нейната оценка
    for jury in range(1, count_jury+1):
        grade = float(input())
        sum_grades += grade # сума от оценки за текуща презентация
        sum_all_grades += grade  #  сума от оценки за всички презентации
        count += 1 #  броя на всички оценки
    average_grade = sum_grades / count_jury
    print(f"{presentation} - {average_grade:.2f}.")
    presentation = input()
else:
    print(f"Student's final assessment is {(sum_all_grades/ count):.2f}." )