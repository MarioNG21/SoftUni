command = input()
contest_pass = {}
while not command == "end of contests":
    cmd_arg = command.split(":")
    contest = cmd_arg[0]
    password = cmd_arg[1]
    contest_pass[contest] = password
    command = input()

new_command = input()
new_dict = {}
while not new_command == "end of submissions":
    cmd_argument = new_command.split("=>")
    contest_new = cmd_argument[0]
    new_pass = cmd_argument[1]
    username = cmd_argument[2]
    points = int(cmd_argument[3])
    if contest_new not in contest_pass or new_pass != contest_pass[contest_new]:
            new_command = input()
            continue
    if username not in new_dict:
        new_dict[username] = {contest_new: points}

    elif contest_new not in new_dict[username]:
        new_dict[username].update({contest_new: points})

    elif new_dict[username][contest_new] < points:
        new_dict[username][contest_new] = points
    new_command = input()

best = {u: sum(i.values()) for u, i in new_dict.items()}

for key, value in best:
    print(f"Best candidate is {key} with total {value} points.")
    break

new_sorting = sorted(new_dict.items(), key=lambda kvp: kvp[0])
for i, j in new_sorting:
    print(f"#  {i} -> {j} ")