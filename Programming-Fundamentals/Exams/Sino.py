time_to_leave = [int(i) for i in input().split(":")]
number_of_steps = int(input())
time_for_one_step = int(input())

time_for_steps_min = (number_of_steps * time_for_one_step) // 60
time_sec = (number_of_steps * time_for_one_step) % 60
time_to_leave_sec = int(time_to_leave[2]) + time_sec
if time_to_leave_sec >= 60:
    time_to_leave[2] += 1
