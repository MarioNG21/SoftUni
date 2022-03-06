message = input()
command = input()
while not command == "Reveal":
    cmd_arg = command.split(":|:")
    action = cmd_arg[0]
    if action == "InsertSpace":
        index = int(cmd_arg[1])
        message_list = list(message)
        message_list.insert(index, " ")
        message = ''.join(message_list)
        print(message)
    elif action == "Reverse":
        sub_str = cmd_arg[1]
        if sub_str in message:
            reversed_sub = sub_str[::-1]
            message = message.replace(sub_str, "", 1)
            message += reversed_sub
            print(message)
        else:
            print("error")
    elif action == "ChangeAll":
        sub = cmd_arg[1]
        replacement = cmd_arg[2]
        message = message.replace(sub, replacement)
        print(message)
    command = input()
print(f"You have a new text message: {message}")