movie_name = input()
type_ticket = input()
bought_tickets = int(input())
income = 0

if movie_name == "A Star Is Born":
    if type_ticket == "normal":
        price = 7.50
        income = price * bought_tickets
    elif type_ticket == "luxury":
        price = 10.50
        income = price * bought_tickets
    elif type_ticket == "ultra luxury":
        price = 13.50
        income = price * bought_tickets
elif movie_name == "Bohemian Rhapsody":
    if type_ticket == "normal":
        price = 7.35
        income = price * bought_tickets
    elif type_ticket == "luxury":
        price = 9.45
        income = price * bought_tickets
    elif type_ticket == "ultra luxury":
        price = 12.75
        income = price * bought_tickets
elif movie_name == "Green Book":
    if type_ticket == "normal":
        price = 8.15
        income = price * bought_tickets
    elif type_ticket == "luxury":
        price = 10.25
        income = price * bought_tickets
    elif type_ticket == "ultra luxury":
        price = 13.25
        income = price * bought_tickets
elif movie_name == "The Favourite":
    if type_ticket == "normal":
        price = 8.75
        income = price * bought_tickets
    elif type_ticket == "luxury":
        price = 11.55
        income = price * bought_tickets
    elif type_ticket == "ultra luxury":
        price = 13.95
        income = price * bought_tickets
print(f"{movie_name} -> {income:.2f} lv.")