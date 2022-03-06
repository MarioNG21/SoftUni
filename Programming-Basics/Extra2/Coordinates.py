season = input()
type_of_group = input()
number_of_students = int(input())
number_of_nights = int(input())

if season == "Winter" and (type_of_group == "boys" or type_of_group == "girls" or type_of_group == "mixed"):
    if type_of_group == "boys" or type_of_group == "girls":
        price = 9.60
    elif type_of_group == "mixed":
        price = 10
    whole_price = price * number_of_students * number_of_nights
    if number_of_students >= 50:
        whole_price *= 0.5
    elif 20 <= number_of_students < 50:
        whole_price *= 0.85
    elif 10 <= number_of_students < 20:
        whole_price *= 0.95
    if type_of_group == "boys":
        sport = "Judo"
    elif type_of_group == "girls":
        sport = "Gymnastics"
    elif type_of_group == "mixed":
        sport = "Ski"
    print(f"{sport} {whole_price:.2f} lv.")
if season == "Spring" and (type_of_group == "boys" or type_of_group == "girls" or type_of_group == "mixed"):
    if type_of_group == "boys" or type_of_group == "girls":
        price = 7.20
    elif type_of_group == "mixed":
        price = 9.50
    whole_price = price * number_of_students * number_of_nights
    if number_of_students >= 50:
        whole_price *= 0.5
    elif 20 <= number_of_students < 50:
        whole_price *= 0.85
    elif 10 <= number_of_students < 20:
        whole_price *= 0.95
    if type_of_group == "boys":
        sport = "Tennis"
    elif type_of_group == "girls":
        sport = "Athletics"
    elif type_of_group == "mixed":
        sport = "Cycling"
    print(f"{sport} {whole_price:.2f} lv.")
if season == "Summer" and (type_of_group == "boys" or type_of_group == "girls" or type_of_group == "mixed"):
    if type_of_group == "boys" or type_of_group == "girls":
        price = 15
    elif type_of_group == "mixed":
        price = 20
    whole_price = price * number_of_students * number_of_nights
    if number_of_students >= 50:
        whole_price *= 0.5
    elif 20 <= number_of_students < 50:
        whole_price *= 0.85
    elif 10 <= number_of_students < 20:
        whole_price *= 0.95
    if type_of_group == "boys":
        sport = "Football"
    elif type_of_group == "girls":
        sport = "Volleyball"
    elif type_of_group == "mixed":
        sport = "Swimming"
    print(f"{sport} {whole_price:.2f} lv.")
