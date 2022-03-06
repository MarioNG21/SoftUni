
def is_out_of_stock(collection: list, gift: str):
    easter_gift = gift
    for el in collection:
        for ch in range(len(collection)):
            if easter_gift == el:
                if easter_gift in collection:
                    collection[ch] = "None"



    return collection


def is_required(collection: list, gift: str, index: int):
    easter_gift = gift
    index_gift = index
    if 0 <= index_gift <= len(collection) - 1:
        for ch in range(len(collection)):
            if index_gift == int(ch):
                collection.pop(ch-1)
                collection.insert(index_gift - 1, easter_gift)

    return collection


def just_in_case(collection: list, gift: str):
    easter_gift = gift
    collection.pop(-1)
    collection.append(easter_gift)

    return collection


presents = input().split()
command = input()

while command != "No Money":
    cmd_arg = command.split()
    command_type = str(cmd_arg[0])
    command_gift = str(cmd_arg[1])
    if command_type == "Required":
        command_index = int(cmd_arg[2])
        is_required(presents, command_gift, command_index)
    elif command_type == "OutOfStock":
        is_out_of_stock(presents, command_gift)
    elif command_type == "JustInCase":
        just_in_case(presents, command_gift)

    command = input()

print(f"{' '.join(presents)}")
