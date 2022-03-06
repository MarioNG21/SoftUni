number_of_pieces = int(input())
pieces_dict = {}

for i in range(number_of_pieces):
    piece, composer, key = input().split('|')
    pieces_dict[piece] = {"Composer": composer, "Key": key}

command = input()
while not command == "Stop":
    cmd_arg = command.split('|')
    action = cmd_arg[0]
    if action == "Add":
        new_piece = cmd_arg[1]
        new_composer = cmd_arg[2]
        new_key = cmd_arg[3]
        if new_piece not in pieces_dict:
            pieces_dict[new_piece] = ({"Composer": new_composer, "Key": new_key})
            print(f"{new_piece} by {new_composer} in {new_key} added to the collection!")
        else:
            print(f"{new_piece} is already in the collection!")
    elif action == "Remove":
        removed_piece = cmd_arg[1]
        if removed_piece in pieces_dict:
            del pieces_dict[removed_piece]
            print(f"Successfully removed {removed_piece}!")
        else:
            print(f"Invalid operation! {removed_piece} does not exist in the collection.")
    elif action == "ChangeKey":
        changed_piece = cmd_arg[1]
        changed_key = cmd_arg[2]
        if changed_piece in pieces_dict:
            pieces_dict[changed_piece]["Key"] = changed_key
            print(f"Changed the key of {changed_piece} to {changed_key}!")
        else:
            print(f"Invalid operation! {changed_piece} does not exist in the collection.")
    command = input()

sorted_list = sorted(pieces_dict.items(), key=lambda kvp: (kvp[0], kvp[1]["Composer"]))

for p, items in sorted_list:
    print(f"{p} -> Composer: {items['Composer']}, Key: {items['Key']}")
