from sys import maxsize
command = input()
max_goals = -maxsize
has_hat_trick = False
last_name = ""
while command != "END":
    name_of_a_player = command
    scored_goals = int(input())
    if scored_goals > max_goals:
        max_goals = scored_goals
        last_name = name_of_a_player
    if scored_goals >= 3:
        has_hat_trick = True
    if scored_goals >= 10:
        break
    command = input()
print(f"{last_name} is the best player!")
if has_hat_trick == True:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")
