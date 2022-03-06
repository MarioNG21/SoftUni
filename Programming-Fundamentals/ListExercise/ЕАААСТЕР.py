presents = input().split()
command = input()
while command != "No Money":
    cmd_arg = command.split()
    cmd_order = cmd_arg[0]
    cmd_gift = cmd_arg[1]

    if cmd_order == "Required":
        cmd_index = int(cmd_arg[2])
        if 0 <= cmd_index <= len(presents) - 1:
            for ch in range(len(presents)):
                if ch == cmd_index:
                    presents[ch] = str(cmd_gift)

    elif cmd_order == "OutOfStock":
        for ch in range(len(presents)):
            gift = presents[ch]
            if gift == cmd_gift:
                presents[ch] = "None"
    elif cmd_order == "JustInCase":
        presents[-1] = cmd_gift

    command = input()

for gifts in presents:
    if gifts != "None":
        presents.append(gifts)

print(f"{' '.join(presents)}")
