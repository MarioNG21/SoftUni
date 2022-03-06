'''

Gemstone  = if 100 <= x <= 199:
Sculture  = elif  200 <= x <= 299:
Gold  =  elif 300 <= x <= 399:
Dimond Jewellery  = elif 400 <= x <= 499:

if gemstone and sculpture -> Win
or gold and jewellery -> Win


first - magic level
last - materials
'''

from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

magic_materials = {}
gem_counter = 0
porcelain_count = 0
gold_counter = 0
diamond_counter = 0
has_won = False

while materials:
    if not magic:
        break
    current_material = materials.pop()
    current_magic = magic.popleft()
    sum_of_both = current_material + current_magic
    if sum_of_both < 100:
        if sum_of_both % 2 == 0:
            sum_of_both = (2 * current_material) + (3 * current_magic)
        elif sum_of_both % 2 == 1:
            sum_of_both *=  2

    elif sum_of_both > 499:
        sum_of_both /= 2

    if 100 <= sum_of_both <= 199:
        el = "Gemstone"
        gem_counter += 1
        if el not in magic_materials:
            magic_materials[el] = 0
        magic_materials[el] += 1
    elif 200 <= sum_of_both <= 299:
        porcelain_count += 1
        el = "Porcelain Sculpture"
        if el not in magic_materials:
            magic_materials[el] = 0
        magic_materials[el] += 1
    elif 300 <= sum_of_both <= 399:
        gold_counter += 1
        el = "Gold"
        if el not in magic_materials:
            magic_materials[el] = 0
        magic_materials[el] += 1
    elif 400 <= sum_of_both <= 499:
        diamond_counter += 1
        el = "Diamond Jewellery"
        if el not in magic_materials:
            magic_materials[el] = 0
        magic_materials[el] += 1

if gem_counter > 0 and porcelain_count > 0:
    has_won = True

elif gold_counter > 0 and diamond_counter > 0:
    has_won = True

if has_won:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials])}")

if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for key, value in sorted(magic_materials.items()):
    print(f"{key}: {value}")
