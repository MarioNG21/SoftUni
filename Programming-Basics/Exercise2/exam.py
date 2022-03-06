exam_hours = int(input())
exam_minutes = int(input())
exam_in_minutes = (exam_hours * 60) + exam_minutes

arrive_hour = int(input())
arrive_minutes = int(input())
arrive_in_minutes = (arrive_hour * 60) + arrive_minutes
if arrive_in_minutes > exam_in_minutes:
    print("Late")
    late_time = arrive_in_minutes - exam_in_minutes
    if late_time < 60:
        print(f"{late_time}minutes after the start")
    else:
        late_time_in_hours = late_time // 60
        late_time_in_minutes = late_time % 60
        if late_time_in_minutes < 10:
            print(f"{late_time_in_hours }: 0{late_time_in_minutes} hours after the start")
        else:
            print(f"{late_time_in_hours}: {late_time_in_minutes} hours after the start")
elif arrive_in_minutes == exam_in_minutes or exam_in_minutes - arrive_in_minutes <= 30:
    print("On time")
    if exam_in_minutes - arrive_in_minutes <= 30 :
        print(f"{exam_in_minutes - arrive_in_minutes} minutes before the start")
elif exam_in_minutes - arrive_in_minutes > 30:
    print("Early")
    # ako podranim s po malko ot 60 min
    early_time = exam_in_minutes - arrive_in_minutes
    if early_time < 60:
        print(f"{early_time}minutes before the start")
    else:
        early_time_in_hours = early_time // 60
        early_time_in_minutes = early_time % 60
        if early_time_in_minutes < 10:
            print(f"{early_time_in_hours }: 0{early_time_in_minutes} hours before the start")
        else:
            print(f"{early_time_in_hours}: {early_time_in_minutes} hours before the start")
