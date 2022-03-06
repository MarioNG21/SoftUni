amount_joinery = int(input())
type_joinery = input()
delivery = input()
price_per_one = 0

if type_joinery == "90X130":
    price_per_one = 110 * amount_joinery
    if 30 <= amount_joinery <= 60:
        price_per_one = price_per_one - 0.05 * price_per_one
    if amount_joinery > 60:
        price_per_one = price_per_one - 0.08 * price_per_one

elif type_joinery == "100X150":
    price_per_one = 140 * amount_joinery
    if 40 < amount_joinery <= 80:
        price_per_one = price_per_one - 0.06 * price_per_one
    if amount_joinery > 80:
        price_per_one = price_per_one - 0.1 * price_per_one

elif type_joinery == "130X180":
    price_per_one = 190 * amount_joinery
    if 20 < amount_joinery <= 50:
        price_per_one = price_per_one - 0.07 * price_per_one
    if amount_joinery > 50:
        price_per_one = price_per_one - 0.12 * price_per_one

elif type_joinery == "200X300":
    price_per_one = 250 * amount_joinery
    if 25 < amount_joinery <= 50:
        price_per_one = price_per_one - 0.09 * price_per_one
    if amount_joinery > 50:
        price_per_one = price_per_one - 0.14 * price_per_one

if delivery == "With delivery":
    price_per_one += 60
else:
    price_per_one = price_per_one

if amount_joinery > 99:
    price_per_one = price_per_one - 0.04 * price_per_one
if amount_joinery < 10:
    print("Invalid order")
    exit()
print(f"{price_per_one:.2f} BGN")
