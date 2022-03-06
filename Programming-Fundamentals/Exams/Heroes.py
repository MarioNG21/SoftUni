number_of_heroes = int(input())

my_hero_party = {}

for n in range(number_of_heroes):
    cmd = input().split()
    name = cmd[0]
    hero_hp = int(cmd[1])
    hero_mana = int(cmd[2])
    my_hero_party[name] = {'Mana': hero_mana, "HP": hero_hp}


command = input()
while not command == "End":
    cmd_arg = command.split(" - ")
    action = cmd_arg[0]
    if action == "CastSpell":
        hero_name = cmd_arg[1]
        needed_mp = int(cmd_arg[2])
        spell = cmd_arg[3]
        if hero_name in my_hero_party:
            if needed_mp <= my_hero_party[hero_name]["Mana"]:
                print(f"{hero_name} has successfully cast {spell} and now has {my_hero_party[hero_name]['Mana'] - needed_mp} MP!")
                my_hero_party[hero_name]["Mana"] = my_hero_party[hero_name]["Mana"]-needed_mp
            else:
                print(f"{hero_name} does not have enough MP to cast {spell}!")
    elif action == "TakeDamage":
        hero = cmd_arg[1]
        damage = int(cmd_arg[2])
        attacker = cmd_arg[3]

        if my_hero_party[hero]["HP"] - damage > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {my_hero_party[hero]['HP']-damage} HP left!")
            my_hero_party[hero]["HP"] = my_hero_party[hero]["HP"] - damage
        else:
            print(f"{hero} has been killed by {attacker}!")
            del my_hero_party[hero]

    elif action == "Recharge":
        name = cmd_arg[1]
        max_mp = 200
        amount = int(cmd_arg[2])
        if my_hero_party[name]["Mana"] + amount > max_mp:
            print(f"{name} recharged for {max_mp-my_hero_party[name]['Mana']} MP!")
            my_hero_party[name]["Mana"] = max_mp
        else:
            print(f"{name} recharged for {amount} MP!")
            my_hero_party[name]["Mana"] = my_hero_party[name]["Mana"] + amount
    elif action == "Heal":
        name = cmd_arg[1]
        amount = int(cmd_arg[2])
        max_hp = 100
        if my_hero_party[name]["HP"] + amount > max_hp:
            print(f"{name} healed for {max_hp - my_hero_party[name]['HP']} HP!")
            my_hero_party[name]["HP"] = max_hp
        else:
            print(f"{name} healed for {amount} HP!")
            my_hero_party[name]["HP"] = my_hero_party[name]["HP"] + amount

    command = input()
for name, items in sorted(my_hero_party.items(), key=lambda kvp: (-kvp[1]["HP"], kvp[0])):
    print(f'{name}')
    print(f'  HP: {items["HP"]}')
    print(f'  MP: {items["Mana"]}')