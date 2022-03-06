from math import ceil
height = int(input())
length = int(input())
unused_part_in_percent = int(input())
command = input()
whole_room = 4 * (height * length) # m^2
whole_room_with_windows = ceil(whole_room - ((unused_part_in_percent/ 100) * whole_room))
left_work = True
left_paint = 0
while command != "Tired!":
    paint = int(command)
    whole_room_with_windows -= paint
    if whole_room_with_windows <= 0:
        left_work = False
        left_paint = abs(whole_room_with_windows)
        break
    command = input()
if left_work:
    print(f"{whole_room_with_windows} quadratic m left.")
else:
    if left_paint != 0:
        print(f"All walls are painted and you have {left_paint} l paint left!")
    else:
        print("All walls are painted! Great job, Pesho!")
