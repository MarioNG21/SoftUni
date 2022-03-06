def is_collected(collection: list,item: str):
    if item not in collection:
        collection.append(item)
    return collection


def is_dropped(collection: list, item:  str):
    if item in collection:
        collection.remove(item)

    return collection


def item_combination(collection: list, old_one: str, new_one: str):
    for ch in range(len(collection)):
        name = collection[ch]
        if name == old_one:
            collection.insert(int(ch+1), new_one)
    return collection


def is_renewed(collection: list, item: str):
    if item in collection:
        collection.remove(item)
        collection.append(item)
    return collection


journal = input().split(", ")
command = input().split(' - ')
while command != ['Craft!']:
    act = command[0]
    if act == "Collect":
        the_item = command[1]
        is_collected(journal, the_item)
    elif act == "Drop":
        dropped_item = command[1]
        is_dropped(journal, dropped_item)
    elif act == "Combine Items":
        new_items = command[1].split(':')
        old_item = new_items[0]
        new_item = new_items[1]
        item_combination(journal, old_item, new_item)
    elif act == "Renew":
        renewed_item = command[1]
        is_renewed(journal, renewed_item)

    command = input().split(" - ")

print(', '.join(journal))