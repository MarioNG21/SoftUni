stops = input()

command = input()
while not command == "Travel":
    cmd_arg = command.split(":")
    action = cmd_arg[0]
    if action == "Add Stop":
        index = int(cmd_arg[1])
        string = cmd_arg[2]
        if 0 <= index <= len(stops) - 1:
            new_stop_list = list(stops)
            new_stop = new_stop_list.insert(index, string)
            stops = ''.join(new_stop_list)

    elif action == "Remove Stop":
        start_index = int(cmd_arg[1])
        end_index = int(cmd_arg[2])
        if 0 <= start_index <= len(stops) - 1 and 0 <= end_index <= len(stops) - 1:
            new = stops[start_index:end_index+1]
            stops = stops.replace(new, "")

    elif action == "Switch":
        old_str = cmd_arg[1]
        new_str = cmd_arg[2]
        if old_str in stops:
            stops = stops.replace(old_str, new_str)

    print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")