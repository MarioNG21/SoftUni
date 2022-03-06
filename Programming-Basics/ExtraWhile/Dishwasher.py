# 750 ml preparat
# 1 chiniq e ravna na 5 ml
# 1 tendjara e 15 ml
# na vsqko treto pulnene e pulna s tendjari a na ostanalite s chenii
number_of_bottles = int(input())
number_of_bottles_in_mls = number_of_bottles * 750
time = 1
sum_of_pots = 0
sum_of_dishes = 0
while number_of_bottles_in_mls >= 0:
    command = input()
    if command == "End":
        break
    dishes = int(command)
    if time % 3 == 0:
        used_ml_from_bottle = dishes * 15
        number_of_bottles_in_mls -= used_ml_from_bottle
        sum_of_pots += dishes
    else:
        used_ml_from_bottle = dishes * 5
        number_of_bottles_in_mls -= used_ml_from_bottle
        sum_of_dishes += dishes
    time +=1
else:
    print(f"Not enough detergent, {abs(number_of_bottles_in_mls)} ml. more necessary!")

if number_of_bottles_in_mls >= 0:
    print("Detergent was enough!")
    print(f"{sum_of_dishes} dishes and {sum_of_pots} pots were washed.")
    print(f"Leftover detergent {number_of_bottles_in_mls} ml.")
