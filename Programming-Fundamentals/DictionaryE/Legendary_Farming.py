def collect_material(key_materials_dict: dict, junk_materials: dict, material: str, qnt:int):
    if material == "shards" or material == "fragments" or material == "motes":
        key_materials_dict[material] += qnt
    else:
        if material not in junk_materials.keys():
            junk_materials[material] = qnt
        else:
            junk_materials[material] += qnt


key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}

item_obtained = ""

while item_obtained == "":
    current_line = input().split()
    for i in range(0, len(current_line), 2):
        material_quantity = int(current_line[i])
        material_name = current_line[i+1].lower()

        collect_material(key_materials, junk, material_name, material_quantity)

        if key_materials["shards"] >= 250:
            item_obtained = "Shadowmourne"
            key_materials["shards"] -= 250
            break
        elif key_materials["fragments"] >= 250:
            item_obtained = "Valanyr"
            key_materials["fragments"] -= 250
            break
        elif key_materials["motes"] >= 250:
            item_obtained = "Dragonwrath"
            key_materials["motes"] -= 250
            break

sorted_dict = sorted(key_materials.items(), key=lambda kvp: (-kvp[1], kvp[0]))

print(f"{item_obtained} obtained!")
for key, value in sorted_dict:
    print(f"{key}: {value}")

for junk_material_name, junk_material_qnt in sorted(junk.items(), key=lambda kvp: kvp[0]):
    print(f"{junk_material_name}: {junk_material_qnt}")
