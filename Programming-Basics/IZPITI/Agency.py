city = input()
package = input()
vip_discount = input()
days = int(input())
price = 0
ok = True
if days < 1:
    print("Days must be positive number!")
    exit()
else:
    if days > 7:
        days += 1
    if city == "Bansko" or city == "Borovets":
        if package == "withEquipment":
            price = 100
            if vip_discount == "yes":
                price = price - 0.10 * price
                price = price * days
            else:
                price = price
                price = price * days
        elif package == "noEquipment":
            price = 80
            if vip_discount == "yes":
                price = price - 0.05 * price
                price = price * days
            else:
                price = price
                price = price * days
        else:
            print("Invalid input!")
            ok = False
            exit()
    elif city == "Varna" or city == "Burgas":
        if package == "withBreakfast":
            price = 130
            if vip_discount == "yes":
                price = price - 0.12 * price
                price = price * days
            else:
                price = price
                price = price * days
        elif package == "noBreakfast":
            price = 100
            if vip_discount == "yes":
                price = price - 0.07 * price
                price = price * days
            else:
                price = price
                price = price * days
        else:
            print("Invalid input!")
            ok = False
            exit()
    else:
        print("Invalid input!")
        ok = False
        exit()
if ok:
    print(f"The price is {price:.2f}lv! Have a nice time!")