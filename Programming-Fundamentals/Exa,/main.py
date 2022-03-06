raw_activation_key = input()

command = input()
while command != "Generate":
    action = command.split(">>>")
    if action[0] == "Contains":
        sub_string = action[1]
        if sub_string in raw_activation_key:
            print(f"{raw_activation_key} contains {sub_string}")
        else:
            print("Substring not found!")
    elif action[0] == "Flip":
        state = action[1]
        start_index = int(action[2])
        end_index = int(action[3])
        first_part = raw_activation_key[:start_index]
        to_change = raw_activation_key[start_index:end_index]
        last_part = raw_activation_key[end_index:]
        if state == "Upper":
            to_change = to_change.upper()
        else:
            to_change = to_change.lower()
        raw_activation_key = first_part + to_change + last_part
        print(raw_activation_key)
    elif action[0] == "Slice":
        start_index = int(action[1])
        end_index = int(action[2])
        first_part = raw_activation_key[:start_index]
        last_part = raw_activation_key[end_index:]
        raw_activation_key = first_part + last_part
        print(raw_activation_key)
    command = input()

print(f"Your activation key is: {raw_activation_key}")