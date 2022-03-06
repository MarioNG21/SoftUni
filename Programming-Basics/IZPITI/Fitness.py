people_in_fitness = int(input())
back = 0
chest = 0
legs = 0
abs = 0
protein_bars = 0
protein_shake = 0
for people in range(1, people_in_fitness+1):
    exercise_done = input()
    if exercise_done == "Back":
        back += 1
    elif exercise_done == "Chest":
        chest += 1
    elif exercise_done == "Legs":
        legs += 1
    elif exercise_done == "Abs":
        abs += 1
    elif exercise_done == "Protein shake":
        protein_shake += 1
    else:
        protein_bars += 1
print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bars} - protein bar")
work_out = back + chest + legs + abs
print(f"{(work_out / people_in_fitness)* 100:.2f}% - work out")
protein = protein_bars + protein_shake
print(f"{(protein / people_in_fitness)* 100:.2f}% - protein")