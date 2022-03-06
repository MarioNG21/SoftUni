# получаваме обем на куфар и обема на всеки трети куфар се + 10%
# ако свободното пространство е по-малко от обема на куфара товаренето прекъсва
capacity = float(input())
command = input()
time = 1
number_of_luggage = 0
luggage = 0
free_space = True
while command != "End":
    luggage = float(command)
    if time % 3 == 0:
        luggage = luggage + 0.1 * luggage
    if luggage > capacity:
        free_space = False
        break
    capacity -= luggage
    time += 1
    number_of_luggage += 1
    command = input()
else:
    print("Congratulations! All suitcases are loaded!")
    print(f"Statistic: {number_of_luggage} suitcases loaded.")
if free_space == False:
    print("No more space!")
    print(f"Statistic: {number_of_luggage} suitcases loaded.")