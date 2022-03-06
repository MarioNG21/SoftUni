import re
command = input()
pattern = r'^>>(?P<furniture_name>[A-Za-z]+)<<(?P<cost>\d+\.?\d*)!(?P<quantity>\d+)$'
total_price = 0
bought_furniture = []
while command != "Purchase":
    match = re.match(pattern, command)
    if match is not None:
        name = match.group('furniture_name')
        price = float(match.group("cost"))
        qty = int(match.group("quantity"))

        total_price += price * qty
        bought_furniture.append(name)
    command = input()

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_price:.2f}")