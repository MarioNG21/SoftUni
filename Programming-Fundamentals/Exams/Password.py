message = input()
command = input()
while not command == "Done":
    cmd_arg = command.split()
    action = cmd_arg[0]
    if action == "TakeOdd":
        new_pass = ""
        for i in range(len(message)):
            word = message[i]
            if i % 2 == 1:
                  new_pass += word
        message = new_pass
        print(message)

    elif action == "Cut":
        index = int(cmd_arg[1])
        length = int(cmd_arg[2])
        cut_message = message[index:]
        new_message = message[:index]
        new_index = 0
        for ch in range(length):
            new_index += 1
        cut_message = cut_message[new_index:]
        message = new_message + cut_message
        print(message)

    elif action == "Substitute":
        sub_str = cmd_arg[1]
        substitute = cmd_arg[2]
        if sub_str in message:
            message = message.replace(sub_str, substitute)
            print(message)
        else:
            print("Nothing to replace!")

    command = input()

print(f"Your password is: {message}")