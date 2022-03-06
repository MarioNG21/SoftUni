def fire(collection: list, index: int, damage: int):
    if index > len(collection) - 1 or index < 0:
        return
    else:
        collection_int = [int(number) for number in collection]
        for chr in range(len(collection)):
            section = collection_int[chr]
            if index == chr:
                section -= damage
                section_str = str(section)
                collection[chr] = section_str
                if section <= 0:
                    return "You won! The enemy ship has sunken."
        return collection


def defend(collection: list, start_index: int, end_index: int, damage: int):

    if (start_index > len(collection)-1 or start_index < 0) or (end_index > len(collection) - 1 or end_index < 0) :
        return
    else:
        collection_int = [int(number) for number in collection]
        for chr in range(start_index, end_index+1):
            section = collection_int[chr]
            section -= damage
            section_str = str(section)
            collection[chr] = section_str
            if section <= 0:
                return "You lost! The pirate ship has sunken."
        return collection


def repair(collection, index: int, health: int, max_health_capacity: int):
    if index > len(collection) - 1:
        return
    else:
        collection_int = [int(number) for number in collection]
        for chr in range(len(collection)):
            section = collection_int[chr]
            if index == chr:
                if section + health > max_health_capacity:
                    section = max_health_capacity
                    collection[chr]= str(section)
                else:
                    section += health
                    collection[chr] = str(section)
        return collection


def status(collection: list, max_health_capacity: int):
    collection_int = [int(number) for number in collection]
    counter = 0
    for chr in range(len(collection)):
        section = collection_int[chr]
        if section < (max_health_capacity * 0.2):
            counter += 1
    return print(f"{counter} sections need repair.")


pirate_shp_status_str = input().split(">")
warship_status_str = input().split(">")

max_health = int(input())
is_stalemate = True
command = input().split()
while command != ["Retire"]:
    cmd_arg = command[0]
    if cmd_arg == "Fire":
        fire_index = int(command[1])
        fire_damage = int(command[2])
        b = fire(warship_status_str, fire_index, fire_damage)
        if b == "You won! The enemy ship has sunken.":
            print("You won! The enemy ship has sunken.")
            is_stalemate = False
            break
    elif cmd_arg == "Defend":
        defend_start_index = int(command[1])
        defend_end_index = int(command[2])
        defend_damage = int(command[3])
        a = defend(pirate_shp_status_str, defend_start_index, defend_end_index, defend_damage)
        if a == "You lost! The pirate ship has sunken.":
            is_stalemate = False
            print("You lost! The pirate ship has sunken.")
            break
    elif cmd_arg == "Repair":
        repair_index = int(command[1])
        repair_health = int(command[2])
        repair(pirate_shp_status_str, repair_index, repair_health, max_health)
    elif cmd_arg == "Status":
        status(pirate_shp_status_str, max_health)

    command = input().split()
if is_stalemate:

    pirate_shp_status_int = [int(number) for number in pirate_shp_status_str]
    warship_status_int = [int(number) for number in warship_status_str]
    sum_pirate = sum(pirate_shp_status_int)
    sum_warships = sum(warship_status_int)
    print(f"Pirate ship status: {sum_pirate}")
    print(f"Warship status: {sum_warships}")