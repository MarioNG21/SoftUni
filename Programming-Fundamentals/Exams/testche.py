total_plants_count, plants = int(input()), {}

for _ in range(total_plants_count):
    plant_name, current_rarity = input().split("<->")
    plants[plant_name] = {"rarity": int(current_rarity), "rating": []}

command = input()
while command != "Exhibition":
    command = command.split(": ")

    if "Rate" in command:
        plant, rating = command[1].split(" - ")
        if plant not in plants:
            print(f"error")
        else:
            plants[plant]["rating"].append(int(rating))

    elif "Update" in command:
        plant, new_rarity = command[1].split(" - ")
        if plant not in plants:
            print(f"error")
        else:
            plants[plant]["rarity"] = int(new_rarity)

    elif "Reset" in command:
        plant = command[1]
        if plant not in plants:
            print(f"error")
        else:
            plants[plant]["rating"].clear()

    command = input()

for pl in plants:
    if not plants[pl]["rating"]:
        plants[pl]["rating"] = [0]

    plants[pl]["rating"] = sum(plants[pl]["rating"]) / len(plants[pl]["rating"])

print(f"Plants for the exhibition:")
for pl, items in sorted(plants.items(), key=lambda x: (-x[1]["rarity"], -x[1]["rating"])):
    print(f"- {pl}; Rarity: {items['rarity']}; Rating: {items['rating']:.2f}")