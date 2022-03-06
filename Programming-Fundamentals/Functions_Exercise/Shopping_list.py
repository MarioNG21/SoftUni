def is_urgent(collection: list, item: str):
    if item not in collection:
        collection.insert(0, item)
    return collection


def is_unnecessary(collection: list, item: str):
    if item in collection:
        collection.remove(item)
    return collection


def is_correct(collection: list, old_one: str, new_one: str):
    for ch in range(len(collection)):
        name = collection[ch]
        if name == old_one:
            collection[ch] = new_one
    return collection


def is_rearrange(collection: list, item: str):
    if item in collection:
        collection.remove(item)
        collection.append(item)


initial_list = input().split("!")
cmd = input()
while cmd != "Go Shopping!":
    command = cmd.split()
    act = command[0]
    if act == "Urgent":
        target = command[1]
        is_urgent(initial_list, target)
    elif act == "Unnecessary":
        unnecessary_item = command[1]
        is_unnecessary(initial_list, unnecessary_item)
    elif act == "Correct":
        old_item = command[1]
        new_item = command[2]
        is_correct(initial_list, old_item, new_item)
    elif act == "Rearrange":
        rearrange_item = command[1]
        is_rearrange(initial_list, rearrange_item)
    cmd = input()

print(', '.join(initial_list))