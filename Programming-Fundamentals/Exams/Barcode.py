import re
number = int(input())

patter = r"(?P<separator>(\@\#+))(?P<product>([A-Z][a-zA-Z0-9]{4,}([A-Z])))(?P=separator)"
for i in range(number):
    text = input()
    matches = re.finditer(patter, text)
    product_group = ''
    counter = 0
    for match in matches:
        product = match.group('product')
        for i in range(len(product)):
            ch = product[i]
            if ch.isdigit():
                product_group += ch
        counter += 1
    if counter == 0:
        print("Invalid barcode")
        continue
    if product_group == "":
        product_group = "00"
    print(f"Product group: {product_group}")