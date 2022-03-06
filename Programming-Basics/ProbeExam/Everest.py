command = input()
day = 1
start_point = 5364
reached_point = False
while command != "END":
    continue_climbing = command
    climbed_meter = int(input())
    if continue_climbing == "Yes":
        day += 1
        if day > 5:
            if start_point >= 8848:
                reached_point = True
            else:
                reached_point = False
            break
        start_point += climbed_meter
    else:
        day += 0
        start_point += climbed_meter
    if start_point >= 8848:
        reached_point = True
        break
    command = input()
if reached_point:
    print(f"Goal reached for {day} days!")
else:
    print("Failed!")
    print(f"{start_point}")