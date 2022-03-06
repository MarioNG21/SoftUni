def is_blacklisted(collection: list, name: str, counter: int):
    for ch in range(len(collection)):
        blacklisted = collection[ch]
        if name == blacklisted:
            collection[ch] = "Blacklisted"
            print(f"{name} was blacklisted.")
            counter += 1
            break
        else:
            print(f"{name} was not found.")
            break
    return collection, name, counter


def error(collection: list, index: int, counter: int):
    if 0 <= index <= len(collection)-1:
        for el in range(len(collection)):
            lost_name = collection[el]
            if el == index:
                if lost_name != "Lost":
                    if lost_name != "Blacklisted":
                        collection[el] = "Lost"
                        counter += 1
                        print(f"{lost_name} was lost due to an error.")
        return collection, index, counter

    else:
        return collection, index, counter


def is_changed(collection: list, index: int, new_name: str):
    if 0 <= index <= len(collection) - 1:
        for el in range(len(collection)):
            current_name = collection[el]
            if el == index:
                collection[el] = new_name
                print(f"{current_name} changed his username to {new_name}.")
                return collection, index, new_name
    else:
        return collection, index, new_name


friends = input().split(", ")
command = input()
lost_counter = 0
blacklisted_counter = 0
while command != "Report":
    cmd_arg = command.split()
    act = cmd_arg[0]
    if act == "Blacklist":
        blacklisted_name = cmd_arg[1]
        d = is_blacklisted(friends, blacklisted_name, 0)
        blacklisted_counter += int(d[2])
    elif act == "Error":
        error_index = int(cmd_arg[1])
        a = error(friends, error_index, 0)
        lost_counter += int(a[2])
    elif act == "Change":
        changed_index = int(cmd_arg[1])
        changed_name = cmd_arg[2]
        is_changed(friends, changed_index, changed_name)

    command = input()


print(f"Blacklisted names: {blacklisted_counter}")
print(f"Lost names: {lost_counter}")
print(' '.join(friends))
