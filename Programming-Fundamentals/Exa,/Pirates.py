date = input()
cities = {}


while not date == "Sail":
    city, population, gold = date.split("||")
    population = int(population)
    gold = int(gold)
    if city not in cities:
        cities[city] = {"population": population, "gold": gold}
    else:
        cities[city]['population'] += population
        cities[city]['gold'] += gold

    date = input()


data = input()
while not data == "End":
    data = data.split('=>')
    if data[0] == "Plunder":
        city = data[1]
        people = int(data[2])
        gold = int(data[3])

        cities[city]["population"] -= people
        cities[city]['gold'] -= gold
        print(f'{city} plundered! {gold} gold stolen, {people} citizens killed.')
        if cities[city]['population'] <= 0 or cities[city]['gold'] <= 0:
            del cities[city]
            print(f"{city} has been wiped off the map!")
    elif data[0] == "Prosper":
        city = data[1]
        gold = int(data[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
            data = input()
            continue
        else:
            cities[city]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")
    data = input()

if not cities:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    sorted_result = sorted(cities.items(), key=lambda tkvp: (-tkvp[1]['gold'], tkvp[0]))
    print(f"Ahoy, Captain! There are {len(sorted_result)} wealthy settlements to go to:")
    for city, data in sorted_result:
        print(f"{city} -> Population: {data['population']} citizens, Gold: {data['gold']} kg")