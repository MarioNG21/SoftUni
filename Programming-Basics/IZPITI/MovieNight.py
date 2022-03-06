price = int(input())
product_price = 0
ticket = 0
other_products = 0
while price > 0:
    product = input()
    if product == "End":
        break
    text_length = len(product)
    if text_length > 8:
        product_price = ord(product[0]) + ord(product[1])
        price -= product_price
        if price >= 0:
            ticket += 1
        else:
            break
    else:
        product_price = ord(product[0])
        price -= product_price
        if price >= 0:
            other_products += 1
        else:
            break
print(f"{ticket}")
print(f"{other_products}")