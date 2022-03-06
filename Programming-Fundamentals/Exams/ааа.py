import re
pattern = r">>(?P<name>([A-Za-z]+))<<(?P<price>(\d+(\.\d+)?))!(?P<qnt>([0-9]+))"
command = input()
bought_items = []
total_price = 0
while command != "Purchase":
    matches = re.finditer(pattern, command)
    for match in matches:
        name = match.group("name")
        price = float(match.group("price"))
        qnt = int(match.group("qnt"))
        total_price += price * qnt
        bought_items.append(name)
    command = input()
print("Bought furniture:")
for i in bought_items:
    print(i)

print(f"Total money spend: {total_price:.2f}")