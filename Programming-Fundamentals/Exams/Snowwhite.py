command = input()
dwarf_dict = {}

while not command == "Once upon a time":
    cmd_arg = command.split(" <:> ")
    name = cmd_arg[0]
    hat_color = cmd_arg[1]
    phys = int(cmd_arg[2])
    if hat_color not in dwarf_dict:
        dwarf_dict[hat_color] = {name: phys}
    elif name in dwarf_dict[hat_color]:
        if phys > dwarf_dict[hat_color][name]:
            dwarf_dict[hat_color][name] = phys
    else:
        dwarf_dict[hat_color].update({name: phys})
    command = input()

new_dict = {}
for c, all in dwarf_dict.items():
    index = len(all)
    new_dict[c] = {index: all.keys()}

for colour, items in dwarf_dict.items():

    for name, ph in sorted(items.items(), key=lambda x: (-x[1], new_dict[-x[0]])):
        print(f"({colour}) {name} <-> {ph}")
