
good_side = {}
while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if '|' in command:
        cmd_arg = command.split(" | ")
        force_side = cmd_arg[0]
        force_user = cmd_arg[1]
        if force_side not in good_side:
            good_side[force_side] = []
            good_side[force_side].append(force_user)
        else:
            if force_user not in good_side[force_side]:
                good_side[force_side].append(force_user)
            else:
                continue
    elif '->' in command:
        cmd_arg = command.split(" -> ")
        force_user = cmd_arg[0]
        force_side = cmd_arg[1]
        if force_side not in good_side:
            good_side[force_side] = []
            good_side[force_side].append(force_user)
        else:
            for key, value in good_side.items():
                for i in value:
                    if i == force_user:
                        good_side[key].remove(force_user)
                        good_side[force_side].append(force_user)
                        break
                    else:
                        good_side[force_side].append(force_user)
                        break
