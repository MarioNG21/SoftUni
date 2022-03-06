total_electron = int(input())


electron_config = []

current_layer = 1

while total_electron > 0:
    current_layer_electrons = 2 * pow(current_layer, 2)

    if total_electron >= current_layer_electrons:
        electron_config.append(current_layer_electrons)
    else:
        electron_config.append(total_electron)

    total_electron -= current_layer_electrons
    current_layer += 1

print(electron_config)