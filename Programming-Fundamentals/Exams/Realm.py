import re
# sorted alphabetically
demon_book = {}

pattern_health = r"((\+\-\*/\.([0-9]+))*)?([A-Za-z])((\+\-\*/\.([0-9]+))*)?"
pattern_damage = r"(\+|\-)*(\d+(\.(\d+))?)"
pattern_symbols = r"((\*)+?)((\/)+)?"

demons = input()
demons = demons.split(", ")
for d in demons:
    d = d.strip()
    demon_health = re.finditer(pattern_health, d)
    sum_of_health = 0
    for i in demon_health:
        sum_of_health += ord(i.group())
    demon_damage = re.finditer(pattern_damage, d)
    sum_of_damage = 0
    for damage in demon_damage:
        if "-" in damage.group():
            sum_of_damage += float(damage.group())
        else:
            sum_of_damage += float(damage.group())

    symbols = re.finditer(pattern_symbols, d)
    for s in symbols:
        if "*" in s.group():
            sum_of_damage *= 2
        elif "/" in s.group():
            sum_of_damage /= 2
    demon_book[d] = {"Damage": sum_of_damage, "HP": sum_of_health}

for name, items in sorted(demon_book.items(), key=lambda kvp: kvp[0]):
    print(f"{name} - {items['HP']} health, {items['Damage']:.2f} damage")