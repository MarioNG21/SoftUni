name_of_player = input()
left_points = 301
count = 0
bad_counter = 0
command = input()
while command != "Retire":
    place = command
    given_points = int(input())
    if place == "Single":
        given_points = given_points
        if given_points > left_points:
            bad_counter += 1
        else:
            left_points -= given_points
            count += 1
    elif place == "Double":
        given_points *= 2
        if given_points > left_points:
            bad_counter += 1
        else:
            left_points -= given_points
            count += 1
    else:
        given_points *= 3
        if given_points > left_points:
            bad_counter += 1
        else:
            left_points -= given_points
            count += 1
    if left_points == 0:
        break
    command = input()
if left_points == 0:
    print(f"{name_of_player} won the leg with {count} shots.")
else:
    print(f"{name_of_player} retired after {bad_counter} unsuccessful shots.")