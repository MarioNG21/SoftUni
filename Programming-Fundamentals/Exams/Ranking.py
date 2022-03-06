first_command = input()
contest_dict = {}
contest_user_pass = {}
best_one = {}
while not first_command == "end of contests":
    contest, password = first_command.split(":")
    contest_dict[contest] = password
    first_command = input()

command = input()
while not command == "end of submissions":
    cmd_arg = command.split("=>")
    new_contest = cmd_arg[0]
    new_pass = cmd_arg[1]
    user = cmd_arg[2]
    points = int(cmd_arg[3])
    if new_contest in contest_dict and new_pass in contest_dict[new_contest]:
        if new_contest not in contest_user_pass:
            contest_user_pass[new_contest] = {user: points}
        elif user not in contest_user_pass[new_contest]:
            contest_user_pass[new_contest].update({user: points})
        else:
            if points > contest_user_pass[new_contest][user]:
                contest_user_pass[new_contest]["Points"] = points

    command = input()

for name, items in contest_user_pass:
        