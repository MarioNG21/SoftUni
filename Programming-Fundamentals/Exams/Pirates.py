command = input()
city_dict = {}
while command != "Sail":
    cities, population, gold = command.split("||")
    if cities not in city_dict:
        city_dict[cities] = {"Population": int(population), "Gold": int(gold)}
    else:
        city_dict[cities]["Population"] += int(population)
        city_dict[cities]["Gold"] += int(gold)
    command = input()

new_command = input()
while not new_command == "End":
    cmd_arg = new_command.split("=>")
    action = cmd_arg[0]
    if action == "Plunder":
        town = cmd_arg[1]
        people = int(cmd_arg[2])
        gold = int(cmd_arg[3])
        if town in city_dict:
            city_dict[town]["Population"] -= people
            city_dict[town]["Gold"] -= gold
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            if city_dict[town]["Population"] <= 0 or city_dict[town]["Gold"] <= 0:
                del city_dict[town]
                print(f"{town} has been wiped off the map!")

    elif action == "Prosper":
        new_town = cmd_arg[1]
        new_gold = int(cmd_arg[2])
        if new_gold < 0:
            print("Gold added cannot be a negative number!" )
            new_command = input()
            continue
        else:
            city_dict[new_town]["Gold"] += new_gold
            print(f"{new_gold} gold added to the city treasury. {new_town} now has {city_dict[new_town]['Gold']} gold.")

    new_command = input()
a = 5
if city_dict != {}:

    print(f"Ahoy, Captain! There are {len(city_dict)} wealthy settlements to go to:")
    for name, items in sorted(city_dict.items(), key=lambda kvp: (-kvp[1]["Gold"], kvp[0])):
        print(f"{name} -> Population: {items['Population']} citizens, Gold: {items['Gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")