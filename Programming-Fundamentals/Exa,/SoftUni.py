import re
pattern = r'([^\|!$%]+)?\%(?P<name>([A-Z][a-z]+))([^\|!$%]+)?\%\<(?P<product>([A-Za-z0-9]+))\>([^\|!$%]+)?\|(?P<count>[0-9])\|([^\|!$%|[0-9]+]+)?(?P<price>([0-9\.*]+))\$'
command = input()
sum_of_all = 0
while not command == "end of shift":
    matches = re.finditer(pattern, command)
    for match in matches:
        name = match.group('name')
        product = match.group('product')
        count = int(match.group('count'))
        price = float(match.group('price'))
        total_price = count * price
        sum_of_all += total_price
        print(f"{name}: {product} - {total_price:.2f}")
    command = input()

print(f'Total income: {sum_of_all:.2f}')

