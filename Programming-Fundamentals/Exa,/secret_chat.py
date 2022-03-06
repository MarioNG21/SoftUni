encrypted_message = input()
command = input()
while not command == "Reveal":
    cmd_arg = command.split(":|:")
    action = cmd_arg[0]
    if action == "InsertSpace":
        needed_index = int(cmd_arg[1])
        encrypted_message = encrypted_message[:needed_index] + " " + encrypted_message[needed_index:]
        print(encrypted_message)
    elif action == "Reverse":
        sub_str = cmd_arg[1]

        old_message = encrypted_message
        encrypted_message = encrypted_message.replace(sub_str, '', 1)

        if old_message == encrypted_message:
            print('error')
            continue
        substr_list = list(sub_str)
        substr_list.reverse()
        substr_reversed = ''.join(substr_list)
        encrypted_message += substr_reversed
        print(encrypted_message)
    elif action == 'ChangeAll':
        sub_str = cmd_arg[1]
        replacement = cmd_arg[2]
        encrypted_message = encrypted_message.replace(sub_str, replacement)
        print(encrypted_message)
    command = input()


print(f'You have a new text message: {encrypted_message}')