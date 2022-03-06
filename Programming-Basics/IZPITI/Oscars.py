actor = input()
starting_points = float(input())
judges = int(input())
earned_points = 0
counter = 0
all_points = 0
while all_points < 1250.5:
    name_judge = input()
    points_judge = float(input())
    length_name = len(name_judge)
    given_points = (length_name * points_judge) / 2
    earned_points += given_points
    all_points = earned_points + starting_points
    counter += 1
    if counter == judges:
        if all_points < 1250.5:
            diff = 1250.5 - all_points
            print(f"Sorry, {actor} you need {diff:.1f} more!")
            break
else:
    print(f"Congratulations, {actor} got a nominee for leading role with {all_points:.1f}!")
