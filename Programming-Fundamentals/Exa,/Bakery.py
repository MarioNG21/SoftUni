stocks = input().split()
bakery_list = {}
searched_product = input().split()
for i in range(0, len(stocks), 2):
    item = stocks[i]
    qnt = stocks[i + 1]
    bakery_list[item] = int(qnt)
for el in searched_product:
    if el in stocks:
        print(f"We have {bakery_list[el]} of {el} left")
    else:
        print(f"Sorry, we don't have {el}")