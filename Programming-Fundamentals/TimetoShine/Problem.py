message = input()
command = input()
while not command == "End":
    cmd_arg = command.split()
    action = cmd_arg[0]
    if action == "Translate":
        char = cmd_arg[1]
        replacement = cmd_arg[2]
        message = message.replace(char, replacement)
        print(message)
    elif action == "Includes":
        string = cmd_arg[1]
        if string in message:
            print("True")
        else:
            print("False")
    elif action == "Start":
        starting_str = cmd_arg[1]
        index = len(starting_str)
        check = message[:index]
        if check == starting_str:
            print("True")
        else:
            print("False")
    elif action == "Lowercase":
        message = message.lower()
        print(message)
    elif action == "FindIndex":
        find_char = cmd_arg[1]
        if find_char not in message:
            max_index = -1
            print(max_index)
            command = input()
            continue
        max_index = 0
        for i in range(len(message)):
            ch = message[i]
            if ch == find_char:
                if i > max_index:
                    max_index = i
        print(max_index)
    elif action == "Remove":
        start_index = int(cmd_arg[1])
        count = int(cmd_arg[2])
        to_remove = message[start_index:]
        to_remove_list = list(to_remove)
        new_list = []
        counter = 0
        for j in range(len(to_remove)):
            removed_ch = to_remove_list[j]
            new_list.append(removed_ch)
            counter += 1
            if counter == count:
                break
        new_list_str = ''.join(new_list)
        message = message.replace(new_list_str, "")
        print(message)

    command = input()
