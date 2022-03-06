def is_looted(collection: list, word_1: str,):
    if word_1 not in collection:
        collection.insert(0, word_1)
    return collection


def is_dropped(collection: list, index_2: int):
    for el in range(len(collection)):
        item = collection[el]
        if not 0 <= index_2 < len(collection) and -len(collection) < index_2 <= -1:
            continue
        else:
            if el == index_2:
                collection.pop(el)
                collection.append(item)

    return collection


def is_stolen(collection: list, count: int):
    if len(collection) <= count:
        return collection and print("Failed treasure hunt.") and exit()
    else:
        for i in range(len(collection)-1, count + 1, -1):
            collection.pop(i)
        return collection


loot_list = input().split('|')
command = input().split()
sum_of_treasure = 0

while command != ["Yohoho!"]:
    cmd_arg = command.pop(0)
    if cmd_arg == "Loot":
       for chr_2 in command:
            item_2 = chr_2
            loot = is_looted(loot_list, item_2)

    elif cmd_arg == "Drop":
        index = int(command[0])
        the_new_list = is_dropped(loot_list, index)

    elif cmd_arg == "Steal":
        number_of_stolen_elements = int(command[0])
        stolen_list = is_stolen(loot_list, number_of_stolen_elements)

    command = input().split()

for el_2 in loot_list:
    sum_of_treasure += len(el_2)
if len(loot_list) > 0:
    average_gain = f"{sum_of_treasure / len(loot_list):.2f}"
    print(loot_list)
    print(f"Average treasure gain: {average_gain} pirate credits.")
