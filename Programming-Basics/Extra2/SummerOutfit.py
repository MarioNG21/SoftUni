

degree = int(input())
day_time = input()
outfit = ""
shoes = ""
if day_time == "Morning":
    if 10 <= degree <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    if 18 < degree <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    if degree >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
if day_time == "Afternoon":
    if 10 <= degree <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    if 18 < degree <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    if degree >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
if day_time == "Evening":
    if 10 <= degree <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    if 18 < degree <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    if degree >= 25:
        outfit = "Shirt"
        shoes = "Moccasins"
print(f"It's {degree} degrees, get your {outfit} and {shoes}.")