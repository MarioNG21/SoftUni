def potion(health: int, max_health: int):
    if max_health + health > 100:
        health = 100 - max_health
        max_health = 100
    else:
        max_health += health

    return print(f"You healed for {health} hp."), max_health, print(f"Current health: {max_health} hp.")


def chest(coins: int):

    return print(f"You found {coins} bitcoins."), coins


def attack(monster: str, damage: int, max_health, room_counter: int):
    if max_health - damage > 0:
        max_health -= damage
        return print(f"You slayed {monster}."), max_health
    else:
        max_health -= damage
        return print(f"You died! Killed by {monster}."), max_health, print(f"Best room: {room_counter}")


dungeon_rooms = input().split("|")
counter = 0
initial_health = 100
bitcoins = 0
has_lost = False
for cmd in dungeon_rooms:
    cmd_arg = cmd.split()
    room_type = cmd_arg[0]
    if room_type == "chest":
        counter += 1
        loot = int(cmd_arg[1])
        c = chest(loot)
        bitcoins += int(c[1])
    elif room_type == "potion":
        counter += 1
        increased_health = int(cmd_arg[1])
        b = potion(increased_health, initial_health)
        initial_health = b[1]

    else:
        counter += 1
        monster_art = room_type
        monster_damage = int(cmd_arg[1])
        a = attack(monster_art, monster_damage, initial_health, counter)
        initial_health = a[1]
        if initial_health <= 0:
            has_lost = True
            break


if has_lost == False:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {initial_health}")